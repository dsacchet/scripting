#!/bin/bash

exiftool -d '%Y%m%d' -p '$CreateDate' "$1" 2> /dev/null
