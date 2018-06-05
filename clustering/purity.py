#!/usr/bin/env python
# coding=utf-8

import os 

path = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"

clusterPath = "/home/chicho/workspace/repackaged/clustering/MeanShift/clusters/"

apkPairs = {}

def getAPKPairs():

    f = open(path)

    lineList = f.readlines()

    for line in lineList:
        line = line.replace("\n","")
        segs = line.split(",")

        oriApk = segs[0]
        repApk = segs[1]

        if not oriApk in apkPairs.keys():
            pairList = []
            pairList.append(repApk)
            apkPairs[oriApk]= pairList

        else:
            tmpList = apkPairs[oriApk]
            tmpList.append(repApk)
            apkPairs[oriApk]=tmpList 


    return apkPairs


def calPurity():

    fileList = os.listdir(clusterPath)
    appClass = getAPKPairs()

    for file in fileList:
        clusters = []
        filePath = os.path.join(clusterPath,file)
        f = open(filePath)
        lineList = f.readlines()
        f.close()
        eachCluster = []
        

        for line in lineList:
            
            if not line.startswith("*"):
                line = line.replace("\n","")
                eachCluster.append(line)
            elif len(eachCluster)!=0 :
                clusters.append(eachCluster)

                eachCluster = []

        
        cnt = 0

        

        for key in appClass.keys():
            eachcnt = 0
            for cluster in clusters:

                if key in cluster:
                    eachcnt +=1 
                    appPairList = appClass[key]

                    for app in appPairList:
                        if app in cluster:
                           eachcnt += 1
            
            cnt += eachcnt 

        purity = (cnt*1.0)/18070
        
        print purity
        purity = 0.0

    
        print filePath 

calPurity()





print "all work is done!"

            


