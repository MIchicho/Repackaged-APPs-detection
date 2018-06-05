#!/usr/bin/env python
# coding=utf-8
import os

APKPath = "/home/chicho/test/gt/"

WPath = "/home/chicho/result/apks/"

outPath = "/home/chicho/result/APK-nofile/"

fileList = os.listdir(outPath)

if not os.path.exists(WPath):
    os.makedirs(outPath)

for filename in fileList:
    APK = filename + ".apk"
    origPath = os.path.join(APKPath,APK)
    cmd = "cp  {0} {1}".format(origPath,WPath)
    os.system(cmd)
    cmd = "now moving {0}".format(APK)
    print(cmd)


print "all work done!"
