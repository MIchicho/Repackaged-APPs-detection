#!/usr/bin/env python
# coding=utf-8
# author   : Chicho
# date     : 2017-07-17
# filename : findActCnt.py     
# function : this file will help us find some problem apks that the 
#            a3e cannot parse them
#            this activity have activities we calculate the number of 
#            activities and create the View Graph and calculate the 
#            isomorphism problem 

'''
1.find the a3e cannot parse apks
2.calculate the activity number 

'''
import os
import xml.dom.minidom



orisatgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/"

oriapkPath = "/home/chicho/workspace/repackaged/result/original/"

repsatgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/"

repapkPath = "/home/chicho/workspace/repackaged/result/repackaged/"



def parseSatg(path,resultPath):

    apkList = os.listdir(path)

    filename = resultPath.split("/")[-2] + "_LOG"

    for apk in apkList:
        satgPath = os.path.join(path,apk)

        if int(os.path.getsize(satgPath)) <= 88:

            apkName = apk.split(".")[0]
            
            cmd = "echo {0}>>{1}".format(apkName,"a3eNoparse")
            os.system(cmd)

            apkPath = os.path.join(resultPath,apkName)

            manifestPath = os.path.join(apkPath,"AndroidManifest.xml")

            if not os.path.exists(manifestPath):
                print "we cannot find manifestPath {0}".format(manifestPath)

                cmd = "echo {0} >> {1}".format(apkName,"findActCnt_WrongLOG")
                os.system(cmd)
                continue 


            try:
                dom = xml.dom.minidom.parse(manifestPath)  
            except:
                pass 


            root = dom.documentElement

            actList = root.getElementsByTagName('activity')

            actCnt = len(actList)
            
            

            cmd = "echo {0},{1} >> {2}".format(apkName,actCnt,filename)
            os.system(cmd)


parseSatg(orisatgPath,oriapkPath)
parseSatg(repsatgPath,repapkPath)

print "all work is done!"










