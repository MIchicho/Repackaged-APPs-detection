#!/usr/bin/env python
# coding=utf-8
import numpy as np
import os

path = "/home/chicho/workspace/repackaged/clustering/Ori_coaseVec.csv"

apkNameList = []
vecList = []




def parseDate():
    f = open(path)
    lineList = f.readlines()

    for line in lineList:
        line = line.replace("\n","")
        segs = line.split(",")

        apkname = segs[0]

        del segs[0]
        
        print "*********"


        segs=map(int,segs)

        print segs

        vector = np.array(segs)

        print vector

        if not apkname in apkNameList:
            apkNameList.append(apkname)
            vecList.append(vector)


def getEuclDist():

    parseDate()

    for i in range(len(apkNameList)):
        filename = "dist" + str(i)
        for j in range(len(apkNameList)):
            
            if (i != j):
    
                dist = np.linalg.norm(vecList[i]-vecList[j])
                cmd = "echo {0},{1},{2}>>{3}".format(apkNameList[i],apkNameList[j],dist,filename)
                os.system(cmd)




getEuclDist()

print "all work is done!"
