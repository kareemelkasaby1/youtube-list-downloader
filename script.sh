#!/bin/bash
YELLOW='\e[1;33m'
RED='\e[1;31m'
BLUE='\e[1;34m'
NC='\033[0m'
SAD='\xF0\x9F\x98\x94'
HP='\xF0\x9F\x98\x83'
LINK=$(cat link.txt)
if [ -z $2 ]
then
    i=1
    printf "\n\n${YELLOW}Downloading video number ${RED}1${NC} ${HP}\n\n"
else
    i="$(($2+2))"
    printf "\n\n${YELLOW}Downloading video number ${RED}$(($2+2))${NC} ${HP}\n\n"
fi

if ! [[ $LINK = *=+([[:digit:]]) ]] 2> /dev/null && ! [[ -z $2 ]]
then
    echo -e $RED
    echo "list end"
    echo -e $NC
    exit
fi
echo -e $BLUE
node youtub-downloader.js $LINK 2> logfile.txt
echo -e $NC
LAST=$(awk '/./{line=$0} END{print line}' logfile.txt)
# while [[ $LAST == \(node:* ]]
while [ -s logfile.txt ]
do
    printf "\n\n${RED}Download faild ${SAD}\nRetry downloading video number ${YELLOW}${i}${NC}\n\n"
    echo -e $BLUE
    node youtub-downloader.js $LINK 2> logfile.txt
    echo -e $NC
    # LAST=$(awk '/./{line=$0} END{print line}' logfile.txt)
done
if [ $1 == "y" ] || [ $1 == "Y" ]
then
    ./convertToMp3.sh
    rm -f /yotube-list-downloader/downloads/*.mp4
fi
> logfile.txt
