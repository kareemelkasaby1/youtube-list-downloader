#!/bin/bash
for f in /yotube-list-downloader/downloads/*.mp4
do
    echo "Converting $f"
    name=`echo "$f" | sed -e "s/.mp4$//g"`
    ffmpeg -y -i "$f" -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 "$name.mp3"
done
