#!/usr/bin/env python
# coding=utf-8
#  @Author   : Chicho
#  @Date     : 2018-04-14
#  @Function : 1. use FSQuaDRA to calculate the similarity of repackaged app pairs
#              We should put this file with the fsquadra.jar

import os  
import time 

start = time.time()
pairPath = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"

outputPath = "/home/chicho/workspace/repackaged/FSquaDRA/similarValue1.csv"

oriPath = "/home/chicho/workspace/repackaged/pairs/original/"

repPath = "/home/chicho/workspace/repackaged/pairs/repackaging/"

f=open(pairPath)

lineList = f.readlines()

f.close()

for line in lineList:
    line = line.replace("\n","")

    segs = line.split(",")

    oriapk = segs[0] + ".apk"
    repapk = segs[1] + ".apk"

    oriapkPath = os.path.join(oriPath,oriapk)
    repapkPath = os.path.join(repPath,repapk)

    cmd = "java -jar fsquadra.jar {0} {1} -o={2}".format(oriapkPath,repapkPath,"pair1")
    os.system(cmd)

    resPath = "/home/chicho/workspace/repackaged/FSquaDRA/pair1"

    f=open(resPath)
    lines = f.readlines() 
    
    for line in lines:
        line = line.replace("\n","")
#        print "*****************"
#        print line
        cmd = "echo {0}>>{1}".format(line,outputPath)
        os.system(cmd)

    f.close()

end =time.time()

elpase = end-start

print elpase
cmd = "echo {0}>>{1}".format(elpase,"Time")
os.system(cmd)

print "all work is done!"

