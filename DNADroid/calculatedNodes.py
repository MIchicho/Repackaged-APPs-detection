#!/usr/bin/env python
# coding=utf-8


import os 

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/original1/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/repackaged1/"

orioutPutPath = "/home/chicho/workspace/repackaged/DNADroid/node/original/"

repoutPutPath = "/home/chicho/workspace/repackaged/DNADroid/node/repackaged/"

outputPath = "/home/chicho/workspace/repackaged/DNADroid/node/"


def calculateNode(path,outputPath):
    apkList = os.listdir(path)

    for apk in apkList:

        apkPath = os.path.join(path,apk)

        f =open(apkPath)

        countList = []

        eachapkoutPutPath = os.path.join(outputPath,apk)

        for line in f.readlines():
            if ":" in line and ";" in line:
                count = int(line.split(";")[1])
                cmd = "echo {0} >> {1}".format(count,"allNodelist")
                os.system(cmd)
                countList.append(count)


        nodeSUM = sum(countList)*1.0
        
        if len(countList) != 0:
            NodeAvg = int(round(nodeSUM/len(countList)))
        
        if len(countList) == 0 or nodeSUM==0:
            cmd = "echo {0} >> {1}".format(apk,"problem.txt")
            os.system(cmd)
            continue

        cmd = "echo {0} >> {1}".format(NodeAvg,"nodeavg.csv")
        os.system(cmd)

        print countList
        print nodeSUM
        print len(countList)
        print NodeAvg

        f.close()


calculateNode(oriPath,orioutPutPath)

calculateNode(repPath,repoutPutPath)

print "all work is done!"



