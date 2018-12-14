#!/usr/bin/env python
# coding=utf-8

import os 

pairPath = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"

path = "/home/chicho/workspace/repackaged/DroidMOSS/code/experiment/pair2.txt" 

fp = open(pairPath)

pairList=fp.readlines()

f = open(path)

parseLineList = f.readlines()

for line in pairList:

    if line not in parseLineList:
        line = line.replace("\n","")
        cmd = "echo {0}>>exception".format(line)
        os.system(cmd)

        print line 



print "all work is done!"

