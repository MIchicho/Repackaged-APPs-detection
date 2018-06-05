#!/usr/bin/env python
# coding=utf-8
import numpy
import os

path = "/home/chicho/workspace/repackaged/clustering/dist/"


fileList = os.listdir(path)



for file in fileList:
    filePath = os.path.join(path,file)

    f=open(filePath)

    lineList = f.readlines()

    f.close()
    
    distDict ={}

    for line in lineList:
        line = line.replace("\n","")
        segs = line.split(",")

        value = float(segs[2])

        del segs[2]

        appPair = ','.join(segs)

        if not appPair in distDict.keys():
            distDict[appPair]=value 

    distList=sorted(distDict.items(), key=lambda x:x[1])

    for element in distList:

        cmd = "echo {0},{1}>>{2}".format(element[0],element[1],file)
        os.system(cmd)


print "all work is done!"

