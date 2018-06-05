#!/usr/bin/env python
# coding=utf-8
import os
import numpy as np 
from sklearn.cluster import DBSCAN
import time 

oriPath = "/home/chicho/workspace/repackaged/clustering/data/Ori_coaseVec.csv"

repPath = "/home/chicho/workspace/repackaged/clustering/data/Rep_coaseVec.csv"


def getData(lines):

    data = []
    apknameList = []

    for line in lines:
        line = line.replace("\n","")
        segs = line.split(",")

        apkname = segs[0]

        del segs[0]

        segs = np.array(map(int,segs))

        if not apkname in apknameList:
            apknameList.append(apkname)
            data.append(segs)


    return (data,apknameList)





def getCluster():
    
    start = time.time()

    orif = open(oriPath)
    repf = open(repPath)

    oriflines = orif.readlines()

    repflines = repf.readlines()

    data = []
    apknameList = []

    oridata,oriapkname = getData(oriflines)
    repdata,repapkname = getData(repflines)

    data += oridata + repdata
    apknameList += oriapkname + repapkname 


    db = DBSCAN(eps=0.3,min_samples=2).fit(np.radians(data))

    labels = db.labels_

    cluster = {}
    dataCluster = {}
    for i in range(len(labels)):
        if not labels[i] == -1:
            label = labels[i]
            tmpcluster = []
            tmpdata = []
            if not label in cluster.keys():
                tmpcluster.append(apknameList[i])
                tmpdata.append(data[i])
                cluster[label]=tmpcluster
                dataCluster[label]=tmpdata 

            else:
                tmpcluster = cluster[label]
                tmpcluster.append(apknameList[i])
                cluster[label]=tmpcluster

                tmpdata = dataCluster[label]
                tmpdata.append(data[i])

                dataCluster[label]=tmpdata 
                

    for key in cluster.keys():
        print key 
        clusterList = cluster[key]
        vectorList = dataCluster[key]

        cmd = "echo *'{0}'>>{1}".format(key,"cluster_03_2")
        os.system(cmd)
        
        cmd = "echo *'{0}'>>{1}".format(key,"VecCluster_03_2")
        os.system(cmd)

        i = 0 
        for apk in clusterList:
            cmd = "echo {0}>>{1}".format(apk,"cluster_03_2")
            os.system(cmd)
            cmd = "echo {0}>>{1}".format(vectorList[i],"VecCluster_03_2")
            os.system(cmd)
            i = i+ 1

    end = time.time()

    elpase = end - start 

    cmd = "echo {0}>>{1}".format(elpase, "time")
    os.system(cmd)

getCluster()


print "all work is done!"






