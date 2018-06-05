#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho 
# date     :  2017-07-17
# running  :  python parseAct.py 
# function :  1. parse the AndroidManifest.xml file and a3e compare the difference 
#             2. find the nodes are less than 2

import os 
import xml.dom.minidom 

orisatgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/"

oriapkPath = "/home/chicho/workspace/repackaged/result/original/"

repsatgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/"

repapkPath = "/home/chicho/workspace/repackaged/result/repackaged/"


def parseManifest(satgPath,apktoolPath):

    apkList = os.listdir(satgPath)

    fileName = apktoolPath.split("/")[-2] + "_APKACTLOG"

    for apk in apkList:

        eachsatgPath = os.path.join(satgPath,apk)

        apkName = apk.split(".")[0]

        print "we are handling the apk {0}".format(apkName)

        eachapkPath = os.path.join(apktoolPath,apkName)

        manifestPath = os.path.join(eachapkPath,"AndroidManifest.xml")

        if not os.path.exists(manifestPath):
            print "We cannot find {0}'s AndroidManifest.xml file".format(apkName)

            cmd = "echo 'cannot find AndroidManifest.xml', {0} >> {1}".format(apkName,"parseAct_wornfLOG")
            os.system(cmd)

        try:
            satgdom = xml.dom.minidom.parse(eachsatgPath)
        except:
            print "we cannot parse satg file of {0}".format(apkName)

            cmd = "echo 'cannot parse satg file of ' {0} ".format(apkName)
            os.system(cmd)
            continue 

        try:
            manDom = xml.dom.minidom.parse(manifestPath)
        except:
            print "we cannot parse satg file of {0}".format(apkName)

            cmd = "echo 'cannot parse satg file of ' {0} ".format(apkName)
            os.system(cmd)
            continue 

        satgroot = satgdom.documentElement 
        
        satgactList = []

        parentActList = satgroot.getElementsByTagName('Activity')

        for activity in parentActList:

            childActList = activity.getElementsByTagName('ChildActivity')

            parentName = activity.getAttribute('name')

            if not parentName in satgactList:
                satgactList.append(parentName)


            for child in childActList:
                childName = child.getAttribute('name')

                if not childName in satgactList:
                    satgactList.append(childName)


        satgCnt = len(satgactList)

        root = manDom.documentElement 

        actList = root.getElementsByTagName('activity')

        actCnt = len(actList)

        
        cmd = "echo {0},{1},{2}>>{3}".format(apkName,actCnt,satgCnt,fileName)
        os.system(cmd)

        if actCnt != satgCnt:
            noequal = apktoolPath.split("/")[-2] + "noequal"
            cmd = "echo {0},{1},{2}>>{3}".format(apkName,actCnt,satgCnt,noequal)
            os.system(cmd)


parseManifest(orisatgPath,oriapkPath)
parseManifest(repsatgPath,repapkPath)

print "all work is done!"
        


