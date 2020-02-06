#!/bin/bash
# Relis le fichier d'evenement d'openhab et renvoie les donnees dans graphite
# Prevu pour des "counter", le script comble les trous entre deux timestamps
# On repasse par MQTT, on pourra nc la ligne directement dans graphite
# 
#_ITEM=C1S03
#_GRAPHITE_TARGET=compteurs.eau.c1s03.volume.max
#_OLD_TIMESTAMP=1579449480
#_OLD_VALUE=188793.0
#
# TODO trouve automatiquement le premier timestamp et la valeur associee :
# TODO  - head de la premier valeur dans les fichiers events
# TODO  - on en deduit le timestamp
# TODO  - whisper-dump du fichier et extraction de la valeur precedente non nulle

_ITEM=$1
_GRAPHITE_TARGET=$2
_OLD_TIMESTAMP=$3
_OLD_VALUE=$4

grep -h " ${_ITEM}" /var/log/openhab2/events.log.1 /var/log/openhab2/events.log | while read line
do
    _DATE=$(echo $line | sed 's@\(.*\) .vent.ItemStateChangedEvent. - .*@\1@')
    _TIMESTAMP=$(date --date "${_DATE}" +%s)
    _TIMESTAMP=$(($_TIMESTAMP-$_TIMESTAMP%60))
    _VALUE=$(echo $line | sed 's@.* to \([0-9]\+\.[0-9]\+\)$@\1@')

    # initialization
    if [ $_OLD_TIMESTAMP -eq 0 ]
    then
        _OLD_TIMESTAMP=$_TIMESTAMP
        _OLD_VALUE=$_VALUE
        continue
    fi

    # fill gap
    while [ ${_OLD_TIMESTAMP} -lt ${_TIMESTAMP} ]
    do
        mosquitto_pub -h 127.0.0.1 -p 1883 -u <user> -P <pass> -t <topic> -m "A|${_GRAPHITE_TARGET}|${_VALUE}|${_OLD_TIMESTAMP}000" 
        echo ${_GRAPHITE_TARGET} ${_OLD_VALUE} ${_OLD_TIMESTAMP}
        _OLD_TIMESTAMP=$(($_OLD_TIMESTAMP+60))
    done
    _OLD_TIMESTAMP=$_TIMESTAMP
    _OLD_VALUE=$_VALUE
done

