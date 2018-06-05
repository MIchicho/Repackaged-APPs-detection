#!/usr/bin/env python
# coding=utf-8
#  Author  : Chicho
#  running : python getAPKInstructionNum.py

#  function  : 1. calculate the total number of the apk file
#              2. draw a picture 

import os

OriPath = "/home/chicho/workspace/repackaged/Juxtapp/original/"

RepPath = "/home/chicho/workspace/repackaged/Juxtapp/repackaged/"

oriList = os.listdir(OriPath)

repList = os.listdir(RepPath)

for apk in oriList:

    apkPath = os.path.join(OriPath,apk)

    f = open(apkPath)

    instruNum = len(f.readlines())

    cmd = "echo {0} >> {1}".format(instruNum,"oriInstrNum.csv")
    os.system(cmd)
    
    f.close()


for apk in repList:

    apkPath = os.path.join(RepPath,apk)
    
    f = open(apkPath)

    instruNum = len(f.readlines())

    cmd = "echo {0} >> {1}".format(instruNum,"repInstrNum.csv")
    os.system(cmd)

    f.close()


print "all work is done!"
