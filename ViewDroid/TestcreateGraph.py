#!/usr/bin/env python
# coding=utf-8
# author    : Chicho
# date      : 2017-06-12
# filename  : createGraph.py
# function  : 1.parse the AndroidManifest.xml file this file is handled by
#               feedQAPKforGaroe.py which are handled by apktool and dex2jar.sh
#               so we need to install the apktool and dex2jar.sh
#             2.parse the satg and construct the ATG the number is beginning 
#               from the MainActivity. If the apk has not MainActivity we
#               parse the APK from the first satg.xml
#             3.print the result
# 
# each graph store in the related sha256.txt 
# store format:
# sha256.txt
# 0 1
# 1 2
#

import os
import sys 
import xml.dom.minidom 

print "Usage:"
print'''
==================================
running : python createGraph.py
you can input different number to choose the different PATH
***************************************
input : 0 -> original APKs
input : 1 -> repackaged APKs
input : 2 -> test PATH
input : 3 -> your PATH
=================================
''' 

print "\n"

input = raw_input("your choice? 0 or 1 or 2 or 3:\n")

while (input != '0') and (input != '1') and (input !='2') and (input !='3'):
    print "You input is wrong!"
    input = raw_input("your choice? 0 or 1 or 2 or 3:\n")


if (input == '0'):
    print "you choose the original path! ... processing..."

    APKPath = "/home/chicho/workspace/repackaged/result/original/" # the APK PATH is the APK have handled by apktool
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/" # a3e
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/graph/original/"

if (input == '1'):
    print "you choose the repackaged path! ...processing..."
    
    APKPath = "/home/chicho/workspace/repackaged/result/repackaged/" # the APK PATH is the APK have handled by apktool
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/" # a3e 
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/graph/repackaged/"



#************************************************
# We parse the AndroidManifest.xml file 
# and find the MainActivity 
#************************************************


def findMainActivity(manifestPath):

    print "we are in findMainActivity"

    findflag = 0
    MainActivity = ""
    actCnt = 0 
    package = ""

    if not os.path.exists(manifestPath):
        return (findflag,MainActivity,actCnt,package)


    try:
        dom = xml.dom.minidom.parse(manifestPath)
    except:
        return (findflag,MainActivity,actCnt,package)

    root = dom.documentElement

    actList = root.getElementsByTagName('activity')

    actCnt = len(actList)

    print "actCnt " + str(actCnt)

    package = root.getAttribute('package')

    for activity in actList:

        if activity.toxml().find("android.intent.action.MAIN")>0 \
           and activity.toxml().find("android.intent.category.LAUNCHER")>0:
            findflag =1
            MainActivity = activity.getAttribute('android:name')

            if MainActivity.startswith("."):
                package = root.getAttribute('package')
                MainActivity = package + MainActivity

            if not '.' in MainActivity:
                MainActivity = package + "." + MainActivity

    return (findflag,MainActivity,actCnt,package)


#*******************************************
# get all the nodes and the Edge
# parse the satg
# Create the ATG 
#*******************************************


def getTheEdgeSet(manifestPath,apkSatgPath):

    print "we are in the getTheEdgeSet"

    findflag,MainActivity,actCnt,package = findMainActivity(manifestPath)

    print "findflag: " + str(findflag)
    print "MainActivity: " + MainActivity
    print "Activity count: " + str(actCnt)

    print "package name: " + package

    EdgeCollection =  []

    edgeDict = {}

    parentActNameCollection = []

    if not os.path.exists(apkSatgPath):
        return (EdgeCollection,edgeDict,parentActNameCollection)

    try:
        dom = xml.dom.minidom.parse(apkSatgPath)
    except:
        return (EdgeCollection,edgeDict,parentActNameCollection)

    root = dom.documentElement

    parentActList = root.getElementsByTagName('Activity')

    startIndex = 0

    # delete the ads

    portion = package.split(".")

    if len(portion) == 3:
        del portion[-1]
    elif len(portion) > 3:
        del portion[-1]
        del portion[-2]
    elif len(portion) <= 2:
        pass 


    package = '.'.join(portion)

    # We should pay attention the package name may not is the 
    # same with some activity 
    # In this situation, we should use the MainActivity's prefix 

    if findflag == 1:
        if not MainActivity.startswith(package):
            portion = MainActivity.split(".")


            del portion[-1]

            package = '.'.join(portion)

    # delete the ad libraries
    tmpEdgeSetList = []
    tmpParentList = []

    for activity in parentActList:
        actName = activity.getAttribute('name')

        if not actName in tmpParentList:
            tmpParentList.append(actName)


        if not actName in tmpEdgeSetList:
            tmpEdgeSetList.append(actName)

        childActList = activity.getElementsByTagName('ChildActivity')

        for child in childActList:
            childName = child.getAttribute('name')

            if not childName in tmpEdgeSetList:
                tmpEdgeSetList.append(childName)


    # some ads' activity only need to declare the main in Manifest file 
    # but when we use the static to generate the ATG we can find the 
    # ads has more edge (Activity) in the graph ATG so we need to relflash
    # the count of the activity 
    # if the A3E can get more Activity we should use the larger number 


    if actCnt < len(tmpEdgeSetList):
        actCnt = len(tmpEdgeSetList)

    print "The final Activity count: " + str(actCnt)


    #MainActivity

    if findflag==1:
        EdgeCollection.append(MainActivity)

        for i in range(actCnt):

            print "i " + str(i)

            for activity in parentActList:
                parentName = activity.getAttribute('name')

                if not parentName.startswith(package):
                    continue 


                childNameList = []

                if parentName == EdgeCollection[startIndex]:

                    if parentName not in parentActNameCollection:
                        parentActNameCollection.append(parentName)

                    childActList = activity.getElementsByTagName('ChildActivity')

                    for child in childActList:
                        childName = child.getAttribute('Name')

                        if childName not in childNameList:
                            childNameList.append(childName)

                        if childName not in EdgeCollection:
                            EdgeCollection.append(childName)

                    edgeDict[parentName]=childNameList


    

            if startIndex < len(EdgeCollection)-1:
                startIndex = startIndex + 1

    elif findflag==0: # We didn't find the MainActivity 

        for activity in parentActList:
            actName = activity.getAttribute('name')

            if not actName.startswith(package):
                continue

            if actName not in parentActNameCollection:
                parentActNameCollection.append(actName)


            childNameList = []

            if actName not in EdgeCollection:
                EdgeCollection.append(actName)

            childActList = activity.getElementsByTagName('ChildActivity')

            for child in childActList:
                childName = child.getAttribute('name')
                if childName not in childNameList:
                    childNameList.append(childName)

                if childName not in EdgeCollection:
                    EdgeCollection.append(childName)


            edgeDict[actName]=childNameList


    return (EdgeCollection,edgeDict,parentActNameCollection)




#********************************************************
# print the result 
#********************************************************

def createData(manifestPath,apkSatgPath,index,apk_satgFile):

    print "we are in createData"

    EdgeCollection,edgeDict,parentActNameCollection=getTheEdgeSet(manifestPath,apkSatgPath)

    apkname = apk_satgFile.split(".")[0] + ".txt"
    apkoutputPath = os.path.join(graphPath,apkname)

    print apkoutputPath 
    
    print EdgeCollection

    print edgeDict

    if len(EdgeCollection)>2:


        for key in parentActNameCollection:
            tmpList = edgeDict[key]

            for child in tmpList:
                sourceName = key
                targetName = child 

                source = EdgeCollection.index(sourceName)
                target = EdgeCollection.index(targetName)

                print "e " + sourceName + " --> " + targetName
                print "e " + str(source) + " --> " + str(target)

                cmd = "echo {0} {1} >> {2}".format(source,target,apkoutputPath)
                os.system(cmd)


if __name__ == '__main__':

    APKList = os.listdir(APKPath)

    index = 0

    for apk in APKList:
        eachApkPath = os.path.join(APKPath,apk)

        manifestPath = os.path.join(eachApkPath,"AndroidManifest.xml")

        apk_satgFile = apk + ".apk.g.xml"

        apkSatgPath = os.path.join(satgPath,apk_satgFile)

        print "***************************"

        print apk_satgFile 

        createData(manifestPath,apkSatgPath,index,apk_satgFile)


        index = index + 1

    
    print "all work is done!"

