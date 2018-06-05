#!/bin/bash

INPUT=$1

if [ $# -lt 1 ]; then
    exit 1
fi

#D1=$(echo $INPUT | awk -F' ' '{print $1}')

D2=$(echo $INPUT | awk -F' ' '{print $2}')

echo $D2>>DBSCAN_60k.txt
