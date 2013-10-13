#!/bin/bash

INFILE=$1

if [ ! -r "${INFILE}" ]
then
	echo "Impossible de lire le fichier source" 1>&2
	exit 1
fi

if [ "x$(file "${INFILE}" | sed "s@^.*JPEG image data.*@JPEG@")" != "xJPEG" ]
then
	echo "Le fichier n'est pas une image" 1>&2
	exit 1
fi

if [ $(strings "${INFILE}" | sed -n "1,4p" | grep "Exif" | wc -l) -ne 1 ]
then
	echo "Pas d'informations exif, impossible de realiser une rotation" 1>&2
	exit 1
fi

ROTATION_INDICE=$(exif -t 0x0112 -m "$INFILE")

case ${ROTATION_INDICE} in
	"bottom - right")
		ROTATE=180
		;;
	"right - top")
		ROTATE=270
		;;
	"left - bottom")
		ROTATE=90
		;;
	"top - left")
		ROTATE=0
		;;
esac

if [ $ROTATE -ne 0 ]
then
	echo "Rotation de l'image ${INFILE} de $ROTATE°"
	convert "${INFILE}" -rotate $ROTATE "${INFILE}.temp"
	mv "${INFILE}.temp" "${INFILE}"
fi
