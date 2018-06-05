#!/bin/bash

INPUT=$1

OUTPUT=$2

if [ $# -lt 1 ]; then
    exit 1
fi

SIGA=$(echo $INPUT | awk -F':' '{print $2}' | awk -F'>' '{print $1}' | awk -F' ' '{print $1}')

SIGB=$(echo $INPUT | awk -F':' '{print $2}' | awk -F'>' '{print $1}' | awk -F' ' '{print $2}' | awk -F'(' '{print $2}')




SIG=$SIGA"("$SIGB

echo $SIG>>$OUTPUT
