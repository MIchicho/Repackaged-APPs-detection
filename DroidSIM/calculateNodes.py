#!/usr/bin/env python
# coding=utf-8
# Author   : Chicho
# Date     : 2017-07-03
# Running  : python calculateNodes.py
# Function : parse the cfg/pdg signature and calculate the node of each app 


import os 

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/original1/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/repackaged1/"

outputPath = "/home/chicho/workspace/repackaged/DroidSIM/node/"


def calculateNode(path,outputPath):
    apkList = os.listdir(path)

    i = 0
    for apk in apkList:

        i = i + 1
        if i == 10:
            break
        print apk 
        apkPath = os.path.join(path,apk)

        f = open(apkPath)

        countList = []
        
        eachapkoutPutPath = os.path.join(outputPath,apk)
        for line in f.readlines():
            if ":" in line and ";" in line:
                count = int(line.split(";")[1])
                cmd = "echo {0} >> {1}".format(count,eachapkoutPutPath)
                os.system(cmd)
                countList.append(count)

        nodeSum = sum(countList)*1.0
        NodeAvg = round(nodeSum/len(countList))

        print countList
        print nodeSum
        print len(countList)
        print NodeAvg

        f.close()



calculateNode(oriPath,outputPath)
print "all work is done!"

