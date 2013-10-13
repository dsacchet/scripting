#!/bin/bash

mencoder "$1" -o "$2" \
	-of lavf \
	-vf scale=320:240 \
	-srate 44100 \
	-oac mp3lame -lameopts abr:br=128 \
	-ovc lavc -lavcopts vcodec=flv:vbitrate=250:mbd=2:mv0:trell:v4mv:cbp:last_pred=3

