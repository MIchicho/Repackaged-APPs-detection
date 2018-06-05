#!/usr/bin/env python
# coding=utf-8
import os
import sys
import zipfile

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
    path = "/home/chicho/test/test/"
    gator_path = "/home/chicho/result/APK"
else:
    path = raw_input("you APK path:\n")
    #judge you input apk_path right
    if not os.path.exists(path):
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)

    gator_path = raw_input("you Output_path: \n")


if not os.path.exists(gator_path):
    os.makedirs(gator_path)

apklist = os.listdir(path)


for APK in apklist:
    #P = os.path.join(path,APK)
    if APK.endswith(".apk"):
        portion = os.path.splitext(APK)

        # rename
        if portion[1] == ".apk":
            newname = portion[0] + ".zip"
            
            apkPath = os.path.join(path,APK)
            newPath = os.path.join(path,newname)
           # os.rename(apkPath,newPath)

        apkname = portion[0]


        # create a path to store each apks
        gator_apk_path = os.path.join(gator_path,apkname) #e.g. /home/chicho/result/APK/ 
        
        cmd = "apktool d {0} {1}".format(apkPath,gator_apk_path)
        os.system(cmd)
        
        os.rename(apkPath,newPath)
        if not os.path.exists(gator_apk_path):
            os.makedirs(gator_apk_path)

        zip_apk_file = os.path.join(path,newname) # get the zip files

        z = zipfile.ZipFile(zip_apk_file, 'r')

        for filename in z.namelist():
            '''
            if filename == "AndroidManifest.xml":
                manifestPath = os.path.join(gator_apk_path, filename)
                f = open(manifestPath, 'w+')
                f.write(z.read(filename))
            '''
            if filename.endswith(".dex"):
                dexfile = "classes.dex"
                classPath = os.path.join(gator_apk_path,"bin/classes")
                if not os.path.exists(classPath):
                    os.makedirs(classPath)

                dexfilepath = os.path.join(classPath,dexfile)
                f = open(dexfilepath, 'w+')
                f.write(z.read(filename))

        os.rename(newPath,apkPath)
        
    else:
        continue


print "all work done!\n"
