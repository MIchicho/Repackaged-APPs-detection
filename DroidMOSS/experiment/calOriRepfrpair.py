#!/usr/bin/env python
# coding=utf-8
#  Author   : Chicho
#  date     : 2017-3-11
#  running  : python calOriRepfrpair.py
#  function : 1. parse the /home/chicho/workspace/repackaged/repackaging_pairs.txt 
#             2. compare their similarity between original apk's opcode and repackaged apks' opcode 
#                all the files stores in Juxtapp file 

import os
import time

path = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"
oriPath = "/home/chicho/workspace/repackaged/Juxtapp/original/"
repPath = "/home/chicho/workspace/repackaged/Juxtapp/repackaged/"

outputPath = "/home/chicho/workspace/repackaged/DroidMOSS/code/experiment/OriRep_result.txt"
start = time.time()
f = open(path)

for line in f.readlines():
    line = line.replace("\n","")
    ori_sha = line.split(",")[0]
    rep_sha = line.split(",")[1]

    oriAPK = ori_sha + ".txt"
    repAPK = rep_sha + ".txt"

    oriAPKPath = os.path.join(oriPath,oriAPK)
    repAPKPath = os.path.join(repPath,repAPK)

    if os.path.isfile(oriAPKPath) and os.path.isfile(repAPKPath):
        cmd = "ssdeep -lrd {0} {1} >> {2}".format(oriAPKPath,repAPKPath,outputPath)
        os.system(cmd)
        tips = "compare {0} {1}".format(ori_sha,rep_sha)
        print tips 
    elif not os.path.isfile(oriAPKPath):
        print oriAPK + "is not exists!..."
    elif not os.path.isfile(repAPKPath):
        print repAPK + "is not exists!..."


end =time.time()

elpase = end - start

print elpase

print "all work is done!"
