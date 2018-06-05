#!/usr/bin/env python
# coding=utf-8
import os

OriPath = "/home/chicho/workspace/repackaged/DroidSIM/original/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged"

oriGraph = "/home/chicho/workspace/repackaged/DroidSIM/graph/original/"

repGraph = "/home/chicho/workspace/repackaged/DroidSIM/graph/repackaged"


oriList = os.listdir(OriPath)


repList = os.listdir(repPath)

oriGList = os.listdir(oriGraph)

repGList = os.listdir(repGraph)

for apk in oriList:

    if apk not in oriGList:

        cmd = "echo {0} >> {1}".format(apk, "orinoexist")
        os.system(cmd)
        print  apk

for apk in repList:

    if apk not in repGList:

        cmd = "echo {0} >> {1}".format(apk,"repnoexist")
        os.system(cmd)

        print apk 

print "all work is done!"


