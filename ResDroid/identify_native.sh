#!/bin/bash

INPUT=./app_3rdmarkets.csv

while read LINE
do
    apktool_output=$(echo $LINE | awk -F',' '{print $2}')
    [ -e $apktool_output/lib ] && find $apktool_output/lib -type f | xargs file
done < $INPUT
