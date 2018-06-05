#!/usr/bin/env python
# coding=utf-8

import os 

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/original/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/repackaged/"

oriOutPutPath = "/home/chicho/workspace/repackaged/DNADroid/filter/nodesL5/original/"

repOutPutPath = "/home/chicho/workspace/repackaged/DNADroid/filter/nodesL5/repackaged/"


def losslessFilter(path,outputPath):

    apkList = os.listdir(path)
    
    
    for apk in apkList:
        
        apkPath = os.path.join(path,apk)

        apkoutputPath = os.path.join(outputPath,apk)


        if os.path.exists(apkoutputPath):
            continue

        f = open(apkPath)

        lineList = f.readlines()

        for line in lineList:
            if ":" in line and ";" in line:
                nodes = int(line.split(";")[1])

                if nodes >= 5:
                    line = line.replace("\n","")
                    cmd = "echo '{0}' >> {1}".format(line,apkoutputPath)
                    os.system(cmd)

        print apk 

        f.close()

losslessFilter(oriPath,oriOutPutPath)
losslessFilter(repPath,repOutPutPath)

print "all work is done!"
