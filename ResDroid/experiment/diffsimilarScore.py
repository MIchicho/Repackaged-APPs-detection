#!/usr/bin/env python
# coding=utf-8

import numpy as np 
import math  
import os 
import time  
from sklearn import preprocessing 

oriPath = "/home/chicho/workspace/repackaged/ResDroid/original.txt"

repPath = "/home/chicho/workspace/repackaged/ResDroid/repackaged.txt"

pairPath = "/home/chicho/workspace/repackaged/ResDroid/repackaging_pairs.txt"

orif = open(oriPath)
oriLines = orif.readlines()

repf = open(repPath)
repLines = repf.readlines()

oriDict = {}
repDict = {}


def Euclidean(vec1,vec2):
#    npvec1,npvec2 = np.array(vec1),np.array(vec2) 
    return math.sqrt(((vec1-vec2)**2).sum())



for line in oriLines:
    line = line.replace("\n","")
    segs = line.split(",")
    apkname = segs[0]
    oriVec = segs[1:]


    print apkname 

    if not apkname in oriDict.keys():
        oriDict[apkname]=oriVec 



for line in repLines:
    line = line.replace("\n","")
    segs = line.split(",")
    apkname = segs[0]
    repVec = segs[1:]

    print apkname

    if not apkname in repDict.keys():
        repDict[apkname]= repVec 


f=open(pairPath)
lines = f.readlines()

for oriapk in oriDict.keys():
    
    try:
        oriVec = oriDict[oriapk]
    except:
        continue 

    for repapk in repDict.keys():
        try:
            repVec = repDict[repapk]
        except:
            continue

        start = time.time()
    
        oriVec=map(int,oriVec)
        repVec=map(int,repVec)

        min_max_scaler = preprocessing.MinMaxScaler()
        oriArray = min_max_scaler.fit_transform(np.array(oriVec))
        repArray = min_max_scaler.fit_transform(np.array(repVec))
    
        sim = Euclidean(oriArray,repArray)
        end = time.time()

        elapse = float(end-start)

        tips = "{0},{1},{2}".format(oriapk,repapk,sim)
        print tips 

        cmd = "echo {0},{1},{2},{3}>>{4}".format(oriapk,repapk,sim,elapse,"diffsimilarScore")
        os.system(cmd)


print "all work is done"





