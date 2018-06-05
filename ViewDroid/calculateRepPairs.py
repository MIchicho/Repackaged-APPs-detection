#!/usr/bin/env python
# coding=utf-8
#  Author   : Chicho
#  Date     : 2017-06-15
#  filename : createGraph.py
#  function : parse the directory /home/chicho/workspace/repackaged/ViewDroid/graph/original/ 
#             and the directory /home/chicho/workspace/repackaged/ViewDroid/graph/repackaged/ 
#       
#             we should find the repackaged pairs

import os 

oriPath = "/home/chicho/workspace/repackaged/ViewDroid/graph/original/"
repPath = "/home/chicho/workspace/repackaged/ViewDroid/graph/repackaged/"

pairPath = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"



f = open(pairPath)

for line in f.readlines():
    line = line.replace("\n","")

    apks =line.split(",")

    oriapk = apks[0] + ".txt"
    repapk = apks[1] + ".txt"

    oriapkPath = os.path.join(oriPath,oriapk)
    repapkPath = os.path.join(repPath,repapk)

    if os.path.exists(oriapkPath) and os.path.exists(repapkPath):
        cmd = "echo {0},{1}>>{2}".format(apks[0],apks[1],"repackagedPairs.txt")
        os.system(cmd)
        print "{0},{1}".format(apks[0],apks[1])


print "all work is done!"
    


