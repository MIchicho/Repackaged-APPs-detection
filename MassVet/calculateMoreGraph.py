#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho
# Date     :  2017-10-07


import os 


path = "/home/chicho/workspace/repackaged/MassVet/UIWeight/vcoreDetail_weight.csv"


graphDict = {}


f=open(path)

flines = f.readlines()

for line in flines:
    line = line.replace("\n","")
    segs = line.split(",")
    apkname = segs[0]

    if not apkname in graphDict.keys():
        graphDict[apkname] = 1
    else:
        graphDict[apkname] +=1


for key in graphDict.keys():
    cmd = "echo {0},{1}>>{2}".format(key,graphDict[key],"graphDict.csv")
    os.system(cmd)


print "all work is done!"
