#!/usr/bin/env python
# coding=utf-8
import os

oriFile = "/home/chicho/workspace/repackaged/DroidSIM/graph/orinoexist"

repFile = "/home/chicho/workspace/repackaged/DroidSIM/graph/repnoexist"

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/original/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged"


oriOutPutPath = "/home/chicho/workspace/repackaged/DroidSIM/graph/ori/"

repOutputPath = "/home/chicho/workspace/repackaged/DroidSIM/graph/rep/"

orif =open(oriFile)

repf = open(repFile)

def moveFile(path,lines,outputPath):

    for line in lines:
        line = line.replace("\n","")

        apkPath = os.path.join(path,line)

        cmd = "cp {0} {1}".format(apkPath,outputPath)
        os.system(cmd)



moveFile(oriPath,orif,oriOutPutPath)

moveFile(repPath,repf,repOutputPath)


print "all work is done!"
