#!/usr/bin/env python
# coding=utf-8
import os

apkPath = "/home/chicho/result/APK_6_LIBRARIES"

sootPath = "/home/chicho/result/sootAndroidOut_6_LIB"

guiList = os.listdir(sootPath)

apkList = os.listdir(apkPath)


for APK in apkList:
    apkname = APK.split("-")[-1]



    for guifile in guiList:
        if guifile.endswith('.xml'):
                guiname = guifile.split("-")[-2]
                

                if guiname == apkname:
                    print apkname 



