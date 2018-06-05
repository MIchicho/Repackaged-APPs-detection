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
    desPath = "/home/chicho/result/APK_10_REF"
    srcPath = "/mnt/chicho/result/APK_10_REF4/"
else:
    srcPath = raw_input("you source gator APK path:\n")
    #judge you input apk_path right
    if not os.path.exists(srcPath):
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)

    desPath = raw_input("you destination gator path: \n")

    if not os.path.exists(desPath):
        print "Cannot find the destination path!"
        sys.exit(1)



#srcPath = "/mnt/grace/result/sootAndroidOut_10_REF/"

#desPath = "/home/chicho/result/sootAndroidOut_10_REF/"

srcLOGPath = os.path.join(srcPath,"LOG")
srcWrongInfoPath = os.path.join(srcPath,"WrongInfo")

desLOGPath = os.path.join(desPath,"LOG")
desWrongPath = os.path.join(desPath,"WrongInfo")

srcxmlfileList = os.listdir(srcPath)
desxmlfileList = os.listdir(desPath)

desfileList = []

for xmlfile in desxmlfileList:
    if (xmlfile.endswith(".xml")):
        xmlname = xmlfile.split("-")
        xmlname.pop()

        xmlname = '-'.join(xmlname)

        desfileList.append(xmlname)


for xmlfile in srcxmlfileList:
    if (xmlfile.endswith(".xml")):
        xmlname = xmlfile.split("-")
        xmlname.pop()
        
        xmlname = "-".join(xmlname)

        if xmlname in desfileList:
            tips = "{0} has already exists!".format(xmlname)
            print tips 
            continue



        xmlPath = os.path.join(srcPath,xmlfile)
        cmd = "mv {0} {1}".format(xmlPath,desPath)
        os.system(cmd)

        tips = "now moving the *{0}*".format(xmlfile)
        print tips
        




srcLOGList = os.listdir(srcLOGPath)
desLOGList = os.listdir(desLOGPath)

for LOG in srcLOGList:
    if LOG in desLOGPath:
        continue 
    logPath = os.path.join(srcLOGPath,LOG)
    cmd = "mv {0} {1}".format(logPath, desLOGPath)
    os.system(cmd)
    tips = "now moving the {0} file".format(logPath)
    print tips




WrongInfoList = os.listdir(srcWrongInfoPath)
desWrongInfoList = os.listdir(desWrongPath)

for WInfo in WrongInfoList:
    if WInfo in desWrongInfoList:
        continue

    Wpath = os.path.join(srcWrongInfoPath, WInfo)
    cmd = "mv {0} {1}".format(Wpath, desWrongPath)
    os.system(cmd)
    tips = "now moving the {0}".format(WInfo)
    print tips






print "all work done!"
