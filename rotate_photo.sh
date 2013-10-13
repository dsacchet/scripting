#!/bin/bash

INFILE=$1
ROTATE=$2

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

if [ "x$ROTATE" != "x90" -a "x$ROTATE" != "x270" -a "x$ROTATE" != "x180" ]
then
	echo "L'argument rotate ne peut valoir que 90, 270 ou 180"
	exit 1
fi

if [ $ROTATE -ne 0 ]
then
	echo "Rotation de l'image ${INFILE} de $ROTATE°"
	convert "${INFILE}" -rotate $ROTATE "${INFILE}.temp"
	mv "${INFILE}.temp" "${INFILE}"
fi
