#!/bin/bash

# used by a custom .desktop Dolphin context menu to convert files
# not sure why it doesn't work inline but whatever

file=$1
ffmpeg -i "$file" "${file%.*}.$2"