#!/usr/bin/env python
# coding=utf-8

import os 

path = "/home/chicho/workspace/repackaged/ViewDroid/moreGraph/createGraphTime.csv"

f = open(path)

lines = f.readlines()

i =0 
while (i<(len(lines))):
    timeList = []
    line = lines[i]
    line = line.replace("\n","")
    segs = line.split(",")
    apkname = segs[0]
    j = i + 1
    time1 = float(segs[1])
    timeList.append(time1)

    line1 = lines[j]
    line1 = line1.replace("\n","")
    segs1 = line1.split(",")
    apk2 = segs1[0]
    time2 = float(segs1[1])
    
    
    
    while(apk2 == apkname and j < len(lines)):

        
        line1 = lines[j]
        line1 = line1.replace("\n","")
        segs1 = line1.split(",")
        apk2 = segs1[0]
        time2 = float(segs1[1])
        timeList.append(time2)
        j = j + 1
    
    i = j
    mintime = min(timeList)
    cmd = "echo {0},{1}>>{2}".format(apkname,mintime,"graphtime.csv")
    os.system(cmd)




f.close()

print "all work is done!"
