#!/usr/bin/env python
# coding=utf-8
'''
@ author   :  Chicho
@ version  :  1.0
@ date     :  2017-07-08 23:37
@ function :  1. extract dexs file from apk files 
                * create a new directory to store all dex files 
@ running  :  python dex_extract.py
'''


import os 
import zipfile 

path = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/apks/"

dexPath = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/dex/"

apklist = os.listdir(path)

if not os.path.exists(dexPath):
    os.makedirs(dexPath)


for APK in apklist:
    
    apkPath = os.path.join(path,APK)

    portion = os.path.splitext(apkPath)

    if portion[1] == '.apk':
        newname = portion[0] + ".zip"

        os.rename(apkPath,newname)

        print "here&******"

        print apkPath

apklist = os.listdir(path)

for apk in apklist:

    apkPath = os.path.join(path,apk)

    if apkPath.endswith(".zip"):

        apkname = portion[0].split("/")[-1]

        z = zipfile.ZipFile(apkPath,'r')

        for filename in z.namelist():
            if filename.endswith('.dex'):
                dexfilename = apkname + ".dex"
                dexfilePath = os.path.join(dexPath,dexfilename)
                f = open(dexfilePath,'w+')
                f.write(z.read(filename))

  #  print "we are handled the {0}".format(portion[0])


print "all work is done!"
