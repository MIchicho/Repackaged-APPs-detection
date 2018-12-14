#!/usr/bin/env python
# coding=utf-8
# Author    : Chicho
# function  : get the number of opcode of all apks

import os 

path = "/home/chicho/workspace/repackaged/Juxtapp/original/"

repPath = "/home/chicho/workspace/repackaged/Juxtapp/repackaged/"

oriAPKList = os.listdir(path)

repAPKList = os.listdir(repPath)


for apk in oriAPKList:
    filePath = os.path.join(path,apk)

    f = open(filePath)

    opcodeCount = len(f.readlines())
    
    apkName = apk.split(".")[0]
    cmd = "echo {0},{1}>>opcodeCount.csv".format(apkName,opcodeCount)
    os.system(cmd)

    tips = "handled " + apkName
    print tips


for apk in repAPKList:
    filePath = os.path.join(repPath,apk)

    f = open(filePath)

    opcodeCount = len(f.readlines())

    apkName = apk.split(".")[0]
    cmd = "echo {0},{1}>>opcodeCount.csv".format(apkName,opcodeCount)
    os.system(cmd)

    tips = "handled " + apkName
    print tips 



print "all work is done!"




