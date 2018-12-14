#!/usr/bin/env python
# coding=utf-8

import os

Oripath = "/home/chicho/workspace/repackaged/result/original/"

repPath = "/home/chicho/workspace/repackaged/result/repackaged/"


oriAPKList=os.listdir(Oripath)

repAPKList=os.listdir(repPath)


# compare the similarity of dex file
for oriAPK in oriAPKList:

    oriAPKdexPath = os.path.join(Oripath,oriAPK,"smali")

    for repAPK in repAPKList:

        repAPKdexPath = os.path.join(repPath,repAPK,"smali")

        cmd = "ssdeep -lrd -t 78 {0} {1} >> resultTest.txt".format(oriAPKdexPath,repAPKdexPath)
        os.system(cmd)

    cmd = "echo '\n' >> resultTest.txt"
    os.system(cmd)

    tip="compare the {0} and {1}".format(oriAPK,repAPK)
    print tip 


print "all work is done"



