#!/bin/bash

SITE=$1
IMAGE=$2
GALLERY=$3
COMMENTAIRE=$4

echo "<a href=\"http://$1/wp-content/uploads/$IMAGE\" rel=\"lightbox[$GALLERY]\" title=\"$COMMENTAIRE\"><img src=\"http://$1/wp-content/uploads/${IMAGE%.jpg}.thumbnail.jpg\" alt=\"$COMMENTAIRE\" /></a>"


