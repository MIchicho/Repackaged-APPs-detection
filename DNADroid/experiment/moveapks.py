#!/usr/bin/env python
# coding=utf-8


import os 

pairpath = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/apk_pairs"

outputPath = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/sig/"

oripath = "/home/chicho/workspace/repackaged/DroidSIM/original/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged/"



f=open(pairpath)

linelist = f.readlines()

for line in linelist:
    segs = line.split(",")

    oriapk = segs[0]+".txt"
    repapk = segs[1]+".txt"

    oriapkPath = os.path.join(oripath,oriapk)
    repapkPath = os.path.join(repPath,repapk)

    cmd = "cp {0} {1}".format(oriapkPath,outputPath)
    os.system(cmd)

    cmd1 = "cp {0} {1}".format(repapkPath,outputPath)
    os.system(cmd1)

print "all work is done!"
