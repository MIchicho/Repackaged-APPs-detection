#!/usr/bin/env python
# coding=utf-8
import os


'''
path = "/home/chicho/result/APK_1_ARCADE/"


apkFileList = os.listdir(path) 


for apkFileDir in apkFileList: 
    if (apkFileDir.startswith('APK')):  #apkFileDir :APK_10_REF 
        apkfilePath = os.path.join(path,apkFileDir)  #apkfilePath = "/home/chicho/result/APK_10_REF/"

        APKList = os.listdir(apkfilePath)  

        mZor apkfile in APKList:  #apkfile = "1-1"
            apkPath = os.path.join(apkfilePath,apkfile)

            smaliPath = os.path.join(apkPath,"smali")

            outAPKPath = os.path.join(outPath,apkFileDir)

            outSmaliPath = os.path.join(outAPKPath,apkfile)

            if not os.path.exists(outSmaliPath):
                os.makedirs(outSmaliPath)

            cmd = "mv {0} {1}".format(smaliPath,outSmaliPath)
            os.system(cmd)

            tips = "now moving the apk **{0}** file".format(apkfile)
            print tips 



print "all work done!"


'''


path = "/home/chicho/result/APK_1_ARCADE/"

apkFileList = os.listdir(path)


def manifest_parse(manifestPath):

    if not os.path.exists(manifestPath):
        return 

    



if __name__ == "__main__":

    for APK in apkFileList:
        apkfilePath = os.path.join(path,APK)

        manifestPath = os.path.join(apkfilePath,"AndroidManifest.xml")
