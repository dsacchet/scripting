#!/bin/bash

export DISPLAY=:0.0
NB=$(find /home/maison/Images/Xscreensaver | wc -l)
DESTDIR=/home/maison/Images
TEMPDIR=$(mktemp -d)

declare -A SIZEX
declare -A SIZEY
declare -A ORIENTATION

for i in {01..06}
do
	OK=0
	while [ $OK -eq 0 ]
	do
		IMAGE=$(find /home/maison/Images/Xscreensaver | sed -n "$(($RANDOM%$NB))p")
		X=$(identify $IMAGE | cut -d " " -f 3 | cut -d "x" -f 1)
		Y=$(identify $IMAGE | cut -d " " -f 3 | cut -d "x" -f 2)
		if [ "$i" = "01" -o "$i" = "03" -o "$i" = "05" ]
		then
			if [ $X -gt $Y ]; then OK=1; fi
			SIZE=853x480
		else
			if [ $X -lt $Y ]; then OK=1; fi
			SIZE=480x853
		fi
	done

	case "$i" in
		"01"|"06")
			DIRECTION=-
			;;
		"03"|"04")
			DIRECTION=
			;;
		"02")
			if [ $(($RANDOM%2)) -eq 0 ]
			then
				DIRECTION=
				DIRECTION02=
			else
				DIRECTION=-
				DIRECTION02=-
			fi
			;;
		"05")
			if [ "$DIRECTION02" = "-" ]
			then
				DIRECTION=
			else
				DIRECTION=-
			fi
			;;
	esac
		
	cp $IMAGE $TEMPDIR/$i.jpg
	convert $TEMPDIR/$i.jpg -resize $SIZE $TEMPDIR/$i-resize.jpg
	convert -border 10x10 -bordercolor "#FFFFFF" $TEMPDIR/$i-resize.jpg $TEMPDIR/$i-resize-border.jpg
	convert $TEMPDIR/$i-resize-border.jpg \( +clone  -background black  -shadow 60x15+15+15 \) +swap -background none -layers merge +repage $TEMPDIR/$i-resize-border-shadow.png
	convert -alpha set -background none $TEMPDIR/$i-resize-border-shadow.png -rotate ${DIRECTION}4 $TEMPDIR/$i-resize-border-shadow-rotate.png
	SIZEX[$i]=$(identify $TEMPDIR/$i-resize-border-shadow-rotate.png | cut -d " " -f 3 | cut -d "x" -f 1)
	SIZEY[$i]=$(identify $TEMPDIR/$i-resize-border-shadow-rotate.png | cut -d " " -f 3 | cut -d "x" -f 2)
	if [ ${SIZEX[$i]} -gt ${SIZEY[$i]} ]
	then
		ORIENTATION=paysage
	else
		ORIENTATION=portrait
	fi
done


convert -size 2560x1440 gradient:'#000-#324669' \
	-page +40+40                                                $TEMPDIR/01-resize-border-shadow-rotate.png \
	-page +$((2560/2-${SIZEX[02]}/2))+40                        $TEMPDIR/02-resize-border-shadow-rotate.png \
	-page +$((2560-${SIZEX[03]}-40))+40                         $TEMPDIR/03-resize-border-shadow-rotate.png \
	-page +40+$((1440-${SIZEY[04]}-40))                         $TEMPDIR/04-resize-border-shadow-rotate.png \
	-page +$((2560/2-${SIZEX[05]}/2))+$((1440-${SIZEY[05]}-40)) $TEMPDIR/05-resize-border-shadow-rotate.png \
	-page +$((2560-${SIZEX[06]}-40))+$((1440-${SIZEY[06]}-40))  $TEMPDIR/06-resize-border-shadow-rotate.png \
	-layers flatten $DESTDIR/background.png

xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -r
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s $DESTDIR/background.png

rm -rf $TEMPDIR
