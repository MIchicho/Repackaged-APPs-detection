#!/usr/bin/env python
# coding=utf-8
import os


path = "/home/chicho/workspace/repackaged/ResDroid/experiment/fpfn/oriPairs"


f=open(path)

exitList = []

lineList = f.readlines()

for line in lineList:

    line = line.replace("\n","")

    segs = line.split(",")

    oriapk = segs[0]

    if oriapk not in exitList:
        exitList.append(oriapk)

        cmd = "echo {0}>>{1}".format(line,'pairs')
        os.system(cmd)

    else:
        continue 


