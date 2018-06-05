#!/usr/bin/env python
# coding=utf-8
import os

new_APKPath = "/home/chicho/result/APK-n"

apk_gt = "/home/chicho/test/apks/"

apk_apktool = "/home/chicho/result/APK/"

outAPKList = os.listdir(apk_apktool)

APKList = os.listdir(apk_gt)

n_o = len(outAPKList)

n_gt = len(APKList)

i=0

j=0

if not os.path.exists(new_APKPath):
    os.makedirs(new_APKPath)

if ( n_o <= n_gt ):
    mincount = n_o
else:
    mincount = n_gt

'''
while ( i < mincount ):
    portion = os.path.splitext(APKList[j])
    apkname = portion[0]
    if (outAPKList[i] == apkname ):
        i = i+1
        j = j+1
    else:
        nodisAPK = os.path.join(apk_gt,APKList[j])
        cmd = "cp {0} {1}".format(nodisAPK, new_APKPath)
        j = j+1
'''

i = 0
for APK in APKList:
    portion = os.path.splitext(APK)
    print portion[0]
    #j = 0
    for filename in outAPKList:
        j = j+1
        if ( filename == portion[0] ):
            break
    if ( j == len(outAPKList) ):
        i = i + 1    
        APKPath = os.path.join(apk_gt,APK)
        cmd = "cp {0} {1}".format(APKPath,new_APKPath)
        os.system(cmd)

print "There are {0} APKs cannot handle by APKtool".format(i)
