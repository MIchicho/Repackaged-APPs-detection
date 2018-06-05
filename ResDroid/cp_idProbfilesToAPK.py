#!/usr/bin/env python
# coding=utf-8
import os

APKPath = "/home/chicho/result/APK-gt/"

namePath = "/home/chicho/result/specific-axample/*id/"

nameList = os.listdir(namePath)

for APKname in nameList:
    portion = os.path.splitext(APKname)
    APK = portion[0]
    oriAPK = os.path.join(APKPath,APK)
    desPath = "/home/chicho/result/APK/"

    cmd = "cp -r {0} {1}".format(oriAPK, desPath)
    os.system(cmd)
