#!/usr/bin/env python
# coding=utf-8
# running  :  python dexSimilarityComparsion.py  threshold
# Author   :  Chicho
# date     :  2017-3-7 
# function :  1. we compare the dex file between the original apks
#             and repackaged apks 
#             2. set the different threshold and get the best result 
#             3. write the report 
# tip      :  we should install the ssdeep first 

import os
import sys

oriPath = "/home/chicho/workspace/repackaged/result/original/"

repPath = "/home/chicho/workspace/repackaged/result/repackaged/"


oriAPKList = os.listdir(oriPath)

repAPKList = os.listdir(repPath)

#resultfileName = "result_" + sys.argv[1] + ".txt"

for oriAPK in oriAPKList:
    oriAPKdexPath = os.path.join(oriPath,oriAPK,"bin/classes","classes.txt")


    for repAPK in repAPKList:
        repAPKdexPath = os.path.join(repPath,repAPK,"bin/classes","classes.txt")

        if os.path.isfile(oriAPKdexPath) and os.path.isfile(repAPKdexPath):
            if len(sys.argv)==1:
                cmd = "ssdeep -lrd  {0} {1}".format(oriAPKdexPath,repAPKdexPath)
                os.system(cmd)
                

            if len(sys.argv)==2:
                threshold = sys.argv[1]
                resultfileName = "result_" + sys.argv[1] + ".txt"
                cmd = "ssdeep -lrds -t {0} {1} {2} >> {3}".format(threshold, oriAPKdexPath,repAPKdexPath,resultfileName)
                os.system(cmd)

            tip = "compare the {0} and {1}".format(oriAPK,repAPK)

        elif not os.path.isfile(oriAPKdexPath):
            print "dex file of " + oriAPK + "does not exists!..."
        elif not os.path.isfile(repAPKdexPath):
            print "dex file of " + repAPK + "does not exists!..."

    break


print "all work is done!"



