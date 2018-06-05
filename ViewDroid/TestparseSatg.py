#!/usr/bin/env python
# coding=utf-8
# author   : Chicho
# date     : 2017-06-15
# filename : python parseSatg.py
# function : 1. get all the graphs from the satg which is handled by a3e 

import os
import sys 
import xml.dom.minidom 


print " Usage:"
print '''
===========================================================
running : python parseSatg.py
you can input different number to choose the different PATH
**********************************************************
input : 0 -> original APKs 
input : 1 -> repackaged APKs 
input : 2 -> test PATH 
input : 3 -> your PATH 
===========================================================
'''


# when we meet some special apps we cp the special app into this path 

print "\n"

input = raw_input("your choice? 0 or 1 or 2 or 3:\n")

while (input != '0') and (input != '1') and (input != '2') and (input != '3'):
    print "your input is wrong!"
    input = raw_input("your choice? 0 or 1 or 2 or 3:\n")


if (input == '0'):
    print "you choose the original path! ...processing... "

    APKPath = "/home/chicho/workspace/repackaged/result/original/" # the APK PATH is the APK have handled by apktool 
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/"
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/moreGraph/original/"

if (input == '1' ):
    print "you choose the repackaged path! ...processing... "

    APKPath = "/home/chicho/workspace/repackaged/result/repackaged/"
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/"
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/moreGraph/repackaged/"


if (input == '2'):
    print "you choose the test Path! ...processing..."

    APKPath = "/home/chicho/test/problem_Test/apk/"
    satgPath = "/home/chicho/test/problem_Test/satg/"
    graphPath = "/home/chicho/test/problem_Test/"


if (input == '3'):
    APKPath = raw_input("you apk PATH:\n")

    satgPath = raw_input("you satg PATH:\n")

    if not (os.path.exists(APKPath) or os.path.exists(satgPath)):
        print "CANNOT find the PATH,please check your input!"
        sys.exit(1)

    graphPath = raw_input("your graph PATH:\n")




#********************************************
# We parse the AndroidManifest.xml file 
# and find the MainActivity
#********************************************

def findMainActivity(manifestPath):

    print "We are in findMainActivity"

    findflag = 0
    MainActivity = ""
    actCnt = 0
    package = ""  #packageName 

    if not os.path.exists(manifestPath):
        print "We didn't find the AndroidManifest.xml file"

        return (findflag,MainActivity,actCnt,package) #packageName


    try:
        dom = xml.dom.minidom.parse(manifestPath)
    except:
        return (findflag,MainActivity,actCnt,package) #packageName


    root = dom.documentElement
    actList = root.getElementsByTagName('activity')

    actCnt = len(actList)
    print "actCnt " + str(actCnt)

    package = root.getAttribute('package')

    for activity in actList:

        if activity.toxml().find("android.intent.action.Main")>0\
           and activity.toxml.find("android.intent.category.LAUNCHER")>0:
            findflag=1
            MainActivity = activity.getAttribute('android:name')


            if MainActivity.startswith("."):
                package = root.getAttribute('package')
                MainActivity = package + MainActivity 


            if not '.' in MainActivity:
                MainActivity = package + "." + MainActivity 


    return (findflag,MainActivity,actCnt,package)



#
#*************************************
# get all the nodes and the Edge 
# parse the satg
# Create the ATG
#*************************************





def getTheEdgeSet(manifestPath,apkSatgPath):

    print "we are in the getTheEdgeSet"

    #invoke 
    findflag,MainActivity,actCnt,package = findMainActivity(manifestPath)

    print "findflag: " + str(findflag)
    print "MainActivity: " + MainActivity
    print "Activity count: " + str(actCnt)

    print "package name: " + package 

    if input=='0':
        cmd = "echo findflag: {0} >> {1}".format(findflag,"ori_parseInfo.txt")
        os.system(cmd)

        cmd = "echo MainActivity: {0} >>{1}".format(MainActivity,"ori_parseInfo.txt")
        os.system(cmd)

        cmd = "echo Activity count: {0}>>{1}".format(actCnt,"ori_parseInfo.txt")
        os.system(cmd)

        cmd = "echo package name: {0}>>{1}".format(package,"ori_parseInfo.txt")
        os.system(cmd)


    if input == '1':
        cmd = "echo findflag:{0}>>{1}".format(findflag,"rep_parseInfo.txt")
        os.system(cmd)

        cmd = "echo MainActivity: {0}>>{1}".format(MainActivity,"rep_parseInfo.txt")
        os.system(cmd)

        cmd = "echo Acticity count: {0}>>{1}".format(actCnt,"rep_parseInfo.txt")
        os.system(cmd)

        cmd = "echo package name: {0}>>{1}".format(package)
        os.system(cmd)


    EdgeCollection = []

    edgeDict = {}

    parentActNameCollection = []

    if not os.path.exists(apkSatgPath):
        print "The satg file not exists!"
        return (EdgeCollection,edgeDict,parentActNameCollection)

    
    try:
        dom = xml.dom.minidom.parse(apkSatgPath)
    except:
        return (EdgeCollection,edgeDict,parentActNameCollection)

    #
    # the format of satg 
    # <ActivityGraph>
    #  <Activity name="com.anddoes.launcher"/>
    #    <ChildActivity name="com.android.launcher2.launcher"/>
    #    <ChildActivity name="com.anddoes.launcher.ApexService">
    # <ActivityGraph>

    root = dom.documentElement

    parentActList = root.getElementsByTagName('Activity')

    tmpEdgeSetNameList = []
    tmpParentNameList = []


    for activity in parentActList:
        actName = activity.getAttribute('name')

        if not actName in tmpParentNameList:
            tmpParentNameList.append(actName)

    

        if not actName in tmpEdgeSetNameList:
            tmpEdgeSetNameList.append(actName)

        childActList = activity.getElementsByTagName('ChildActivity')

        for child in childActList:
            childName = child.getAttribute('name')

            if not childName in tmpEdgeSetNameList:
                tmpEdgeSetNameList.append(childName)

        

#    if actCnt < len(tmpEdgeSetList):
#        actCnt = len(tmpEdgeSetList) 

    
    #tmpEdgeSetList stores the all the Vex 
    #actually the tmpEdgeSetList is vexsetList
        
    # something wrong for the satg parsing 
    if not MainActivity in tmpEdgeSetNameList:
        findflag = 0

    if not MainActivity in tmpParentNameList:
        findflag = 0 


    if input == '0':
        noparsePath = "/home/chicho/workspace/repackaged/ViewDroid/noParse_or"
    elif input == '1':
        noparsePath = "/home/chicho/workspace/repackaged/ViewDroid/noParse_re"


    if len(tmpEdgeSetNameList) == 0:
        # apkSatgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/000595C346096B92B073F3A7C055FFE466EDCF3E51E017C280FEAB641E3D95D3.apk.g.xml"
        # we split the path and get eachsatgPath = "000595C346096B92B073F3A7C055FFE466EDCF3E51E017C280FEAB641E3D95D3.apk.g.xml"
        eachsatgPath = os.path.split(apkSatgPath)[-1]
        apkname = eachsatgPath.split(".")[0] # get the apkname = 000595C346096B92B073F3A7C055FFE466EDCF3E51E017C280FEAB641E3D95D3.apk.g.xml
        cmd = "echo {0} >> {1}".format(apkname,noparsePath)
        os.system(cmd)

        return (EdgeCollection,edgeDict,parentActNameCollection)



    actCnt = len(tmpEdgeSetNameList)

    
    startIndex = 0
    tmpParentActList = parentActList

    if findflag == 1:
        EdgeCollection.append(MainActivity)

        for i in range(actCnt):

            for activity in tmpParentActList:
                parentName = activity.getAttribute('name') # parentActList=[MA,C2,C1]
                                                           # parentActList=[C2,MA]
                childNameList = []                         # parentActList=[C1,MA],[MA,C1]


                if parentName.startswith('com.google.ads'):
                    continue


                if parentName == EdgeCollection[startIndex]: # parentActList = [MA,C1,C2,C3,C4]

                    if parentName not in parentActNameCollection: # the first time use parentActNameCollection
                        parentActNameCollection.append(parentName)

                    #first time the startIndex = 0 and we put the MainActivity in to the EdgeCollection(the vex collection)
                    # EdgeCollection= [MainActivity]
                    # parentActNameCollection = [MA]
                    # if parentName == MainActivity we should put all their children into the EdgeCollection

                    childActList = activity.getElementsByTagName('ChildActivity')

                    for child in childActList:
                        childName = child.getAttribute('name')

                        if childName not in childNameList:
                            childNameList.append(childName)


                        if childName not in EdgeCollection:
                            EdgeCollection.append(childName)
                            # EdgeCollection = [MA,C1,C2]

                            # p: C2
                            # C: C3, C4 

                    if not parentName in edgeDict.keys():
                        edgeDict[parentName]=childNameList
                        tmpParentActList.remove(activity)  # e.g. we delete the MainActivity

                

                    if startIndex < len(EdgeCollection)-1:
                        startIndex = startIndex + 1

                    break # this is very import tmpParentActList=[C2,C1]

                elif not EdgeCollection[startIndex] in parentActList:
                    if startIndex < len(EdgeCollection)-1:
                        startIndex = startIndex + 1
            
            if tmpParentActList == []:
                break 



        if len(tmpParentActList)>0:

            for activity in tmpParentActList:
                parentName = activity.getAttribute('name')

                if parentName.startswith('com.google.ads'):
                    continue

                if parentName not in 



    
    

        
    elif findflag==0:
        EdgeCollection.append(parentActList[0])
        

        for i in range(actCnt):

            for activity in parentActList:
                parentName = activity.getAttribute('name')

                if parentName.startswith('com.google.ads'):
                    continue


                childNameList = []

                if parentName == EdgeCollection[startIndex]:

                    if not parentName in parentActNameCollection:
                        parentActNameCollection.append(parentName)

                    childActList = activity.getElementsByTagName('ChildActivity')

                    for child in childActList:
                        childName = child.getAttribute('name')

                        if not childName in childNameList:
                            childNameList.append(childName)

                        if not childName in EdgeCollection:
                            EdgeCollection.append(childName)


                    if not parentName in edgeDict.keys():
                        edgeDict[parentName]=childNameList 
                        

                    if startIndex<len(EdgeCollection)-1:
                        startIndex = startIndex + 1

                    break 
                
                elif not EdgeCollection[startIndex] in parentActList:
                    if startIndex < len(EdgeCollection)-1:
                        startIndex = startIndex + 1


    return (EdgeCollection,edgeDict,parentActNameCollection)



#********************************
#  print the result 
#********************************

def createData(manifestPath,apkSatgPath,apk_satgFile):

    print "we are in createData"
    

    EdgeCollection,edgeDict,parentActNameCollection = getTheEdgeSet(manifestPath,apkSatgPath)

    print EdgeCollection

    print edgeDict 

    print parentActNameCollection

    if (input=='0'):

        cmd = "echo {0} >>{1}".format(EdgeCollection,"ori_parseInfo.txt")
        os.system(cmd)

        cmd = "echo {0} >> {1}".format(edgeDict,"ori_parseInfo.txt")
        os.system(cmd)
        
        cmd = "echo {0} >> {1}".format(parentActNameCollection,"ori_parseInfo.txt")
        os.system(cmd)

    if (input=='1'):
        cmd = "echo {0}>>{1}".format(EdgeCollection,"rep_parseInfo.txt")
        os.system(cmd)

        cmd = "echo {0} >>{1}".format(edgeDict,"rep_parseInfo.txt")
        os.system(cmd)

        cmd = "echo {0} >>{1}".format(parentActNameCollection,"rep_parseInfo.txt")
        os.system(cmd)









if __name__ == '__main__':

    APKList = os.listdir(APKPath)

    for apk in APKList:
        eachAPKPath = os.path.join(APKPath,apk)

        manifestPath = os.path.join(eachAPKPath,"AndroidManifest.xml")

        if not os.path.exists(manifestPath):
            print "the manifestPath is not exists!"
            continue


        apk_satgFile = apk + ".apk.g.xml"

        apkSatgPath = os.path.join(satgPath,apk_satgFile)

        if not os.path.exists(apkSatgPath):
            print "the apk Satg file is not exists!"
            continue 



        print "********************************"
        print apk_satgFile

        createData(manifestPath,apkSatgPath,apk_satgFile)



    print "all work is done!"

        
