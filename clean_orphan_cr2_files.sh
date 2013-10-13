#!/bin/bash

find . -name "*.CR2" | while read file; do if [ -f ${file%%.CR2}.dng ]; then rm -f $file; fi; done;
