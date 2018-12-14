#!/usr/bin/env python
# coding=utf-8
# running  : python parseResult.py
# Author   : Chicho
# date     : 2017-3-7
# function : 1. parse the result file similar.txt
#            2. get the result and store the result into the file result.txt

'''
the file similar.txt store the dex similarity result 
in this situation, we should parse the similar.txt first
the format like this 

/original/sha256/bin/classes/classes.dex matches /repackaged/sha256/bin/classes/classes.dex (100)
 
I will parse the file and get the format like following format 

original sha256 repackaged sha256 100 

'''
import os

path = "/home/chicho/workspace/repackaged/DroidMOSS/code/similar.txt"

outPutPath ="/home/chicho/workspace/repackaged/DroidMOSS/code/"

f=open(path)


for line in f.readlines():

    if line.startswith("/home"):
        arr1=line.split()[0]
        arr2=line.split()[2]
        arr3=line.split()[3]

        classname1 = arr1.split("/")[6]
        app1_sha256 = arr1.split("/")[7]

        classname2 = arr2.split("/")[6]
        app2_sha256 = arr2.split("/")[7]

        similarValue = arr3.split("(")[1].split(")")[0]

        if classname1.startswith("original"):
            cmd="echo {0} {1} {2} {3} {4}>>result.txt".format(classname1,app1_sha256,classname2,app2_sha256,similarValue)
            os.system(cmd)

            tips = "we are handle the app" + app1_sha256 + " " + app2_sha256
            print tips

f.close()

print "all work is done!"

