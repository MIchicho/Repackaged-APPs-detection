#!/usr/bin/env python
# coding=utf-8
import os

APKPath = "/home/chicho/result/APK-gt/"

WPath = "/home/chicho/result/bug-cl/no-file/"

outPath = "/home/chicho/result/APK-nofile/"

fileList = os.listdir(WPath)

if not os.path.exists(outPath):
    os.makedirs(outPath)

for filename in fileList:
    portion = os.path.splitext(filename)
    fileLog = portion[0]
    APK = os.path.join(APKPath,fileLog)
    cmd = "cp -r {0} {1}".format(APK,outPath)
    os.system(cmd)
    cmd = "now moving {0}".format(fileLog)
    print(cmd)


print "all work done!"

