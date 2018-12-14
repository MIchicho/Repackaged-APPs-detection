#!/usr/bin/env python
# coding=utf-8
#  Author    : Chicho
#  date      : 2017-3-13
#  function  : 1.compare the ground truth and find the similarity 
#              2. get the TP, TN, FP,FN etc.

import os 

oriPath = "/home/chicho/workspace/repackaged/Juxtapp/original/"

repPath = "/home/chicho/workspace/repackaged/Juxtapp/repackaged/"

oriAPKList = os.listdir(oriPath)
repAPKList = os.listdir(repPath)

for oriAPK in oriAPKList:

    oriAPKPath = os.path.join(oriPath,oriAPK)

    for repAPK in repAPKList:

        repAPKPath = os.path.join(repPath,repAPK)
        
        if os.path.isfile(oriAPKPath) and os.path.isfile(repAPKPath):
            cmd = "ssdeep -lrd {0} {1} >> gtResult.txt".format(oriAPKPath,repAPKPath)
            os.system(cmd)
        elif not os.path.isfile(oriAPKPath):
            tips = oriAPKPath + " not exists!..."
            cmd = "echo {0} >>GTWrongInfo".format(tips)
            os.system(cmd )
        elif not os.path.isfile(repAPKPath):
            tips = repAPKPath + " not exists!..."
            cmd = "echo {0} >>GTWrongInfo".format(tips)
            os.system(cmd)


print "all work is done!"

