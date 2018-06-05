#!/usr/bin/env python
# coding=utf-8
# running   : python getTestSample.py
# function  : Copy some test samples form the Juxtapp analysis result 
#             Juxtapp parse some apps and extract their opcodes
#             1. we first parse the repackage_pairs.txt file the ground truth
#             the repackage_pairs.txt store in the ~/workspace/repackaged/repackaging_pairs.txt 
#             2. copy the repackaged apps from the Juxtapp to DroidMOSS/testSample 
#
# author    : Chicho

import os

gtFilePath = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"

sourcePath = "/home/chicho/workspace/repackaged/Juxtapp/repackaged/"

outputPath = "/home/chicho/workspace/repackaged/DroidMOSS/code/testSample/repackaged/"

f=open(gtFilePath)

for line in f.readlines():
    if line.startswith("9CC2EAEF8636AE77794"):
        line = line.replace("\n","")
        repAPK = line.split(",")[1]

        repAPKName = repAPK + ".txt"

        repAPKPath = os.path.join(sourcePath,repAPKName)

        cmd = "cp {0} {1}".format(repAPKPath,outputPath)
        os.system(cmd)
        
        tip = "move " + repAPK
        print tip 



print "all work is done!"

