#!/bin/bash

model=$(exiftool -p '$Model' "$1" 2> /dev/null)

case "$model" in
	"Canon PowerShot S100")
		echo 'S100';
		;;
	"Canon EOS 40D")
		echo '40D';
		;;
	"GT-I9000")
		echo 'Galaxy S';
		;;
	"Canon EOS 7D")
		echo '7D';
		;;
	"COOLPIX S30")
		echo 'Coolpix S30'
		;;
	"GT-I9300")
		echo 'Galaxy S3'
		;;
	*)
		echo "Autres"
		;;
esac
