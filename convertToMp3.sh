#!/bin/bash
YELLOW='\e[1;33m'
RED='\e[1;31m'
BLUE='\e[1;34m'
GREEN='\e[1;32m'
NC='\033[0m'
HP='\xF0\x9F\x98\x83'
for f in /yotube-list-downloader/downloads/*.mp4
do
    mp4File="$(echo $f | cut -f4 -d"/")"
    mp3File="$(echo $mp4File | cut -f1 -d".")"
    printf "\n\n${YELLOW}Converting ${RED}$mp4File ${YELLOW}to ${GREEN}$mp3File.mp3${NC}  ${HP}\n\n"
    name=`echo "$f" | sed -e "s/.mp4$//g"`
    echo -e $BLUE
    ffmpeg -y -i "$f" -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 "$name.mp3"
    echo -e $NC
done
