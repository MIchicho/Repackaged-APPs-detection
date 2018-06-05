#!/usr/bin/env python
# coding=utf-8

# Author   :  Chicho
# Date     :  2017-10-02
# filename :  getWeight.py
# running  :  python getWeight.py 
# function :  1. parse the a3e and get the active widget 
#             all the active widgets is the weight of its nodes


import os 
import sys
import xml.dom.minidom
import time 

print "Usage:"

print '''
===============================================================
running : python createATGraph.py 
you can input different number to choose the different path
***************************************************************
input : 0 -> original APKs
input : 1 -> repackaged APKs 
input : 2 -> test path 
===============================================================
'''

print "\n"


input = raw_input("your choice? 0 or 1 or 2:\n")


while (input != '0') and (input !='1') and (input != '2'):
    print "your input is wrong!"
    input = raw_input("you choice? 0 or 1 or 2:\n")




if (input == '0'):
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/"
    weightPath = "/home/chicho/workspace/repackaged/MassVet/UIWeight/original/"

if (input == '1'):
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/"
    weightPath = "/home/chicho/workspace/repackaged/MassVet/UIWeight/repackaged/"

if (input == '2'):
    satgPath = "/home/chicho/test/problem_Test/satg/"
    
    weightPath = "/home/chicho/test/problem_Test/UIWeight"





if not os.path.exists(weightPath):
    os.makedirs(weightPath)


def parseWeight(satgPath,weightPath):

    print "we are in the parseWeight"

    satgList = os.listdir(satgPath)

    for satg in satgList:
        eachsatgPath = os.path.join(satgPath,satg)


        try:
            dom = xml.dom.minidom.parse(eachsatgPath)
        except:
            return 

        root = dom.documentElement

        parentActList = root.getElementsByTagName('Activity')

        parentActNameCollection = []

        weightDict = {}

        for activity in parentActList:
            parentName = activity.getAttribute('name')

            #delete the ads
            if parentName.startswith('com.google.ads'):
                continue 

            if parentName.startswith('com.admob.android'):
                continue 

            if parentName.startswith('com.umeng'):
                continue

            if parentName.startswith('com.inmobi'):
                continue 

            if parentName.startswith('com.yume'):
                continue

            if parentName.startswith('com.kiwi.ads'):
                continue 

            if parentName.startswith('com.pontiflex'):
                continue 

            if parentName.startswith('com.adsdk'):
                continue

            if parentName.startswith('com.gfan.sdk'):
                continue 

            if parentName.startswith('com.facebook'):
                continue

            if not parentName in parentActNameCollection:
                parentActNameCollection.append(parentName)


            childActList = activity.getElementsByTagName('ChildActivity')

            if not parentName in weightDict.keys():
                weightDict[parentName] = len(childActList)


        print satg 
        print weightDict 




parseWeight(satgPath,weightPath)
print "all work is done!"
