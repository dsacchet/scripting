#!/bin/bash

if [ $# -ne 2 ]
then
	echo "Usage : outlook2mbox <path to outlook folders> <path to destination mbox file>"
	exit 1
fi

SOURCE="$1"
DEST="$2"

if [ ! -d "$SOURCE" ]
then
	echo "The first paramater must be a directory"
	exit 1
fi

(find "$SOURCE" -depth -type d) | while read sourcedir;
do
	destdir=${DEST}`echo "$sourcedir" | sed "s@^$SOURCE@@" | sed "s@/@.sbd/@g"`
	destfile=`echo "$destdir" | sed 's@.sbd$@@'`
	mkdir -p "$destdir.sbd"
	touch "$destfile"
	(find "$sourcedir" -type f -maxdepth 1) | while read eml;
	do
		DATE=`egrep '^Date: ' "$eml" | sed 's@Date: \(...\), \(..\) \(...\) \(....\) \(........\).*@\1 \3 \2 \4 \5@'`
		DATE=`echo $DATE | sed 's@Date: \(...\), \(.\) \(...\) \(....\) \(........\).*@\1 \3 0\2 \4 \5@'`
		FROM=`egrep 'From: ' "$eml" | sed 's@From: [^<]*<\([^>]*\)>.*@From: \1@' | sed 's@From: @@'`
		echo $FROM
		
		echo "From $FROM $DATE" >> "$destfile"
		cat "$eml" >> "$destfile"
		echo >> "$destfile"
	done;
done;
