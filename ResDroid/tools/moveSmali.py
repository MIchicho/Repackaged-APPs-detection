#!/usr/bin/env python
# coding=utf-8
import os

path = "/home/chicho/result/"

outPath = "/mnt/chicho/APK"

apkFileList = os.listdir(path) 


for apkFileDir in apkFileList: 
    if (apkFileDir.startswith('APK')):  #apkFileDir :APK_10_REF 
        apkfilePath = os.path.join(path,apkFileDir)  #apkfilePath = "/home/chicho/result/APK_10_REF/"

        APKList = os.listdir(apkfilePath)  

        for apkfile in APKList:  #apkfile = "1-1"
            apkPath = os.path.join(apkfilePath,apkfile)

            smaliPath = os.path.join(apkPath,"smali")

            if not os.path.exists(smaliPath):
                tips = "the smali file {0} has already moved!".format(smaliPath)
                print tips
                continue


            outAPKPath = os.path.join(outPath,apkFileDir)

            outSmaliPath = os.path.join(outAPKPath,apkfile)

            if not os.path.exists(outSmaliPath):
                os.makedirs(outSmaliPath)

            cmd = "rm -rf {0}".format(smaliPath)
            os.system(cmd)

            tips = "now moving the apk **{0}** file".format(apkPath)
            print tips 



print "all work done!"

