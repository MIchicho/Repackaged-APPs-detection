#!/bin/bash

INPUT=$1
OUTPUT=$2

if [ $# -lt 1 ]; then
    exit 1
fi

A=$(grep ".xml" $INPUT | awk -F':' '{print $2}' | awk -F'/' '{print $3}' | awk -F'xml' '{print $1}')

B=$(grep ".xml" $INPUT | awk -F':' '{print $2}' | awk -F'/' '{print $3}' | awk -F'xml' '{print $1}' | awk -F'-' '{print $1}')

GUIgraphPath="/tmp/"$A"xml"

#oriFile=$OUTPUT$B".txt"

if [ $GUIgraphPath != "/tmp/xml" ]
then
    mv $GUIgraphPath $OUTPUT
    echo "now it is moving the "$GUIgraphPath" file"
else
    echo "Something Wrong, Gator didn't generate any GUIHierarchy file!"
fi
