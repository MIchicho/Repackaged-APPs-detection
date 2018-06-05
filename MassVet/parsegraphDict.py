#!/usr/bin/env python
# coding=utf-8


import os 

path = "/home/chicho/workspace/repackaged/MassVet/graphDict.csv"


graphCntDict = {}

f =open(path)

flines = f.readlines()

for line in flines:
    line = line.replace("\n","")
    segs = line.split(",")

    key = segs[1]

    if not key in graphCntDict.keys():
        graphCntDict[key] = 1
    else:
        graphCntDict[key] += 1 




for key in graphCntDict.keys():
    cmd = "echo {0},{1}".format(key,graphCntDict[key])
    os.system(cmd)



print "all work is done!"
