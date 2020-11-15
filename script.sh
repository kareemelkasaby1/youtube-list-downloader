#!/bin/bash
exec &>> logfile.txt
LINK=$(cat link.txt)
echo $LINK
if ! [[ $LINK = *=+([[:digit:]]) ]] 2> /dev/null && ! [[ -z $2 ]]
then
    echo "list end"
    exit
fi
node youtub-downloader.js $LINK
LAST=$(awk '/./{line=$0} END{print line}' logfile.txt)
while [[ $LAST == \(node:* ]]
do 
    node youtub-downloader.js
    LAST=$(awk '/./{line=$0} END{print line}' logfile.txt)
done
if [ $1 == "y" ] || [ $1 == "Y" ]
then
    ./convertToMp3.sh
    rm -f ./downloads/*.mp4
fi





# #!/bin/bash
# exec &>> logfile.txt
# echo $3
# echo $2
# if ! [[ $3 = *=+([[:digit:]]) ]] 2> /dev/null && ! [[ -z $2 ]]
# then
#     echo "list end"
#     exit
# fi
# node youtub-downloader.js $3
# LAST=$(awk '/./{line=$0} END{print line}' logfile.txt)
# while [[ $LAST == \(node:* ]]
# do 
#     node youtub-downloader.js
#     LAST=$(awk '/./{line=$0} END{print line}' logfile.txt)
# done
# if [ $1 == "y" ] || [ $1 == "Y" ]
# then
#     ./convertToMp3.sh
#     rm -f ./downloads/*.mp4
# fi
# # > logfile.txt