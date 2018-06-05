#!/usr/bin/env python
# coding=utf-8
import os

path = "/home/chicho/result/sootAndroidOut/"

WrongPath = os.path.join(path,"WrongInfo")

if not os.path.exists(WrongPath):
    os.makedirs(WrongPath)
    

fileList = os.listdir(path)

for filename in fileList:
    filePath = os.path.join(path,filename)
    if (os.path.isfile(filePath)):
        fileSize = os.path.getsize(filePath)
        if (fileSize == 0):
            cmd = "rm {0}".format(filePath)
            os.system(cmd)
        if (filename.endswith(".txt")):
            cmd = "mv {0} {1}".format(filePath,WrongPath)
            os.system(cmd)
