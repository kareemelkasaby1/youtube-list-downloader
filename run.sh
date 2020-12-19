#!/bin/bash

docker run -u `id -u`  -v /dev/shm:/dev/shm  -v $1:/yotube-list-downloader/downloads -it kareemelkasaby/youtube-list-downloader:latest