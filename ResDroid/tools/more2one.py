#!/usr/bin/env python
# coding=utf-8

import os
import sys



print'''
================================================
You can use the default apk files's path or input the path you like!
usage: python feedQAPKforGator.py <apk_path> <Output_path>
Example : python feedQAPKforGator.py /home/chicho/test/APK /home/chicho/test/Output_path
Input : 0 -> default path
Input : 1 -> you personal path
================================================
'''



input = raw_input("you choice ? 0 or 1:\n")

while (input != '0') and (input != '1'):
    print "you input is wrong!"
    input = raw_input("you choice ? 0 or 1:\n")

if (input == '0'):
    print "you choose the default path! ...processing...\n"
    despath = "/home/chicho/result/APK_10_REF"
    srcpath = "/mnt/chicho/result/APK_10_REF4/"
else:
    srcpath = raw_input("you source APK path:\n")
    #judge you input apk_path right
    if not os.path.exists(srcpath):
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)

    despath = raw_input("you destination path: \n")

apkList = os.listdir(srcpath)


for APK in apkList:
    apkPath = os.path.join(srcpath,APK)
    cmd = "mv {0} {1}".format(apkPath,despath)
    os.system(cmd)
    tips = "now moving the {0}".format(apkPath)
    print tips 


cmd = "rm -rf {0}".format(srcpath)
os.system(cmd)
print "remove the {0}".format(srcpath)


print "\n ...all works done!\n"
