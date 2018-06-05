#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho
# Date     :  2017-10-25
# Function :  1. parse the file /home/chicho/workspace/repackaged/ResDroid/original.txt 
#             2. parse the file /home/chicho/workspace/repackaged/ResDroid/repackaged.txt 

#             3. calculate the similarity of the statistic vector between the ori and repackaged 


# 计算 有多少向量的统计特征是没有发生改变的

oriPath = "/home/chicho/workspace/repackaged/ResDroid/original.txt"

repPath = "/home/chicho/workspace/repackaged/ResDroid/repackaged.txt"

pairPath = "/home/chicho/workspace/repackaged/ResDroid/repackaging_pairs.txt"


import os
import numpy

f=open(pairPath)

lineList = f.readlines()

orif = open(oriPath)
oriLineList = orif.readlines()


repf = open(repPath)
repLineList = repf.readlines()

oriDict = {}
repDict = {}

for oriline in oriLineList:
    line = oriline.replace("\n","")
    orivec = line.split(",")
    oriapk = orivec[0]
    del orivec[0]
    
    print "original apps:"
    print oriapk
    print orivec
    
    orivec = map(int,orivec)
    
    print orivec 
    if oriapk not in oriDict.keys():
        oriDict[oriapk]=numpy.array(orivec)


for repline in repLineList:
    line = repline.replace("\n","")
    repvec = line.split(',')
    repapk = repvec[0]

    del repvec[0]

    print "repackaged app"
    print repapk
    print repvec 

    repvec=map(int,repvec)
    print "repackaged apps:"
    print repapk 
    print repvec 

    if repapk not in repDict.keys():
        repDict[repapk]=numpy.array(repvec)


for line in lineList:
    line = line.replace("\n","")

    segs = line.split(",")

    oriapk = segs[0]
    repapk = segs[1]


    if oriapk in oriDict.keys() and repapk in repDict.keys():
        orivec = oriDict[oriapk]
        repvec = repDict[repapk]
        
        print "******************"
        print orivec 
        print repvec 

        dist = numpy.linalg.norm(orivec-repvec)


        cmd = "echo {0},{1},{2}>>{3}".format(oriapk,repapk,dist,"simstaticVec.csv")
        os.system(cmd)



print "all work is done!"
