#!/usr/bin/env python
# coding=utf-8

import os
import sys
import xml.dom.minidom 


APKPath = "/home/chicho/test/problem_Test/apk/"
satgPath = "/home/chicho/test/problem_Test/satg/"
graphPath = "/home/chicho/test/problem_Test/"


#*****************************************
# We parse the AndroidManifest.xml file
# and find the MainActivity
#*****************************************

def findMainActivity(manifestPath):

    print "We are in findMainActivity!"

    findflag = 0
    MainActivity = ""
    package = "" # packageName 

    if not os.path.exists(manifestPath):
        print "We didn't find the AndroidManifest.xml file!"

        return (findflag,MainActivity,package)


    try:
        dom = xml.dom.minidom.parse(manifestPath)
    except:
        return (findflag,MainActivity,package)


    root = dom.documentElement

    actList = root.getElementsByTagName('activity')



    package = root.getAttribute('package')

    for activity in actList:

        if activity.toxml().find("android.intent.action.MAIN")>0\
           and activity.toxml().find("android.intent.category.LAUNCHER")>0:
            findflag=1
            MainActivity = activity.getAttribute('android:name')


            if MainActivity.startswith("."):
                MainActivity = package + MainActivity

            if not '.' in MainActivity:
                MainActivity = package + "." + MainActivity



    return (findflag,MainActivity,package)


def getTheEdgeSet(manifestPath,apkSatgPath):

    print "We are in the getTheEdgeSet"

    findflag,MainActivity,package = findMainActivity(manifestPath)

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


    root = dom.documentElement

    parentActList = root.getElementsByTagName('Activity')

    tmpEdgeSetNameList = []
    tmpParentNameList = []





