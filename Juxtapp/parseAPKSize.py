#!/usr/bin/env python
# coding=utf-8
# Author    :  Chicho
# running   :  python parseAPKSize.py
# Date      :  2017-05-04
# function  :  1. parse the size file and get a statistical range
#              2. draw a picture


import os 


oriPath = "/home/chicho/workspace/repackaged/Juxtapp/code/originalSize.csv"

repPath = "/home/chicho/workspace/repackaged/Juxtapp/code/repackagedSize.csv"


orif = open(oriPath)

repf = open(repPath)

histDist={}

for line in orif.readlines():

    line = line.replace("\n","")

    size = int(line)

    range = size / 10000

    if range not in histDist.keys():
        histDist[range] = 1
    else:
        histDist[range] += 1


for key, value in histDist.items():
    cmd = "echo {0},{1} >> {2}".format(key,value,"oriHistSize.csv")
    os.system(cmd)

    print key, value 



histDist = {}

for line in repf.readlines():
    line = line.replace("\n","")
    size = int(line)
    key = size / 10000

    if key not in histDist.keys():
        histDist[key] = 1
    else:
        histDist[key] += 1


for key, value in histDist.items():
    cmd = "echo {0},{1} >> {2}".format(key,value,"repHistSize.csv")
    os.system(cmd)

    print key, value 


print "all work is done!"
