#!/usr/bin/env python
# coding=utf-8

import os

Oripath = "/home/chicho/workspace/repackaged/DroidMOSS/code/testSample/original/"

repPath = "/home/chicho/workspace/repackaged/DroidMOSS/code/testSample/repackaged/"


oriAPKList=os.listdir(Oripath)

repAPKList=os.listdir(repPath)


# compare the similarity of dex file
for oriAPK in oriAPKList:

    oriAPKdexPath = os.path.join(Oripath,oriAPK)

    for repAPK in repAPKList:

        repAPKdexPath = os.path.join(repPath,repAPK)

        cmd = "ssdeep -lrd -t 40 {0} {1} >> resultTest.txt".format(oriAPKdexPath,repAPKdexPath)
        os.system(cmd)

    cmd = "echo '\n' >> resultTest.txt"
    os.system(cmd)

    tip="compare {0}  {1}".format(oriAPK,repAPK)
    print tip 


print "all work is done"



