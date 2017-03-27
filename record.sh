#!/bin/bash

amixer -c 1 set MIC 10%
arecord -D plughw:1,0 -r 16000 -f S16_LE -c 1 -d 10 "message.wav"
 
