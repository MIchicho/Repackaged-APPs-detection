#!/usr/bin/env python
# coding=utf-8
import os
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import datasets

from sklearn.cluster import DBSCAN
from sklearn import metrics


path = "/home/chicho/workspace/repackaged/clustering/Ori_coaseVec.csv"

f=open(path)

lineList = f.readlines()

data = []
for line in lineList:

    line = line.replace("\n","")

    segs = line.split(",")

    del segs[0]

    segs = np.array(map(int,segs))

    data.append(segs)

    

db=DBSCAN(eps=0.3,min_samples=10).fit(np.radians(data))

print db


