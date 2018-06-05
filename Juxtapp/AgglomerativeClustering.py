#!/usr/bin/env python
# coding=utf-8
import os 
import numpy as np 
from sklearn.cluster import AgglomerativeClustering
import time 

oriPath = "/home/chicho/workspace/repackaged/clustering/data/Ori_coaseVec.csv"

repPath = "/home/chicho/workspace/repackaged/clustering/data/Rep_coaseVec.csv"

path = "/home/chicho/workspace/repackaged/Juxtapp/reData.csv"

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
    orif = open(path)


    oriflines = orif.readlines()
    

    data = []
    apknameList = []

    oridata,oriapkname = getData(oriflines)
    

    data += oridata
    apknameList += oriapkname 

    ac = AgglomerativeClustering(n_clusters=500).fit(data)

    labels = ac.labels_


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

        cmd = "echo *'{0}'>>{1}".format(key,"cluster500")
        os.system(cmd)
        
        cmd = "echo *'{0}'>>{1}".format(key,"VecCluster500")
        os.system(cmd)

        i = 0 
        for apk in clusterList:
            cmd = "echo {0}>>{1}".format(apk,"cluster500")
            os.system(cmd)
            cmd = "echo {0}>>{1}".format(vectorList[i],"VecCluster500")
            os.system(cmd)
            i = i + 1
    
    end = time.time()

    elapse = end - start 

    cmd = "echo {0}>>{1}".format(elapse,'time')
    os.system(cmd)


getCluster()


print "all work is done!"


