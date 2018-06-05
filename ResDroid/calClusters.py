#!/usr/bin/env python
# coding=utf-8
#  Author   :  Chicho
#  date     :  2017-08-12
#  running  :  python calClusters.py 
#  function :  1. create a dictionary to store the clusters 
#              2. parse the repackaging pair filter 

# note the clusters.csv stores the clusters of GT
import os 

path = "/home/chicho/workspace/repackaged/ResDroid/repackaging_pairs.txt"


clusterDict = {}

f=open(path)

lines = f.readlines()

for line in lines:
    line = line.replace("\n","")

    segs = line.split(",")

    oriapk = segs[0]

    if not oriapk in clusterDict.keys():
        clusterDict[oriapk] = 1
    else:
        clusterDict[oriapk] += 1



for key in clusterDict.keys():
    value = clusterDict[key]

    cmd = "echo {0},{1}>>{2}".format(key,value,"clusters.csv")
    os.system(cmd)



print "all work is done!"



