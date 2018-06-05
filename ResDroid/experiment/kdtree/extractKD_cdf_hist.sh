#!/bin/bash

INPUT=$1


if [ $# -lt 1 ];then
    exit 1
fi

D2=$(echo $INPUT | awk -F':' '{print $2}' | awk -F'\' '{print $1}')

if [ "$D2" != "1" ];then
    echo $D2
    echo $D2>>kdtreeoutput.txt
fi

echo $D2>>kdtreeoutput.txt
