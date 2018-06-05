#!/usr/bin/env python
# coding=utf-8
#  Author     :  Chicho
#  Date       :  2015-05-14
#  Running    :  python calculateCFG.py
#  Function   :  calculate the total number of ground truth Apps
#                Draw the Histogram

import os

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/original"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged"

orioutputPath = "/home/chicho/workspace/repackaged/DroidSIM/ori_nodelete_CFG.txt"

repoutputPath = "/home/chicho/workspace/repackaged/DroidSIM/rep_bodelete_CFG.txt"


def calculateCFG(path,outputPath):
    apkList = os.listdir(path)

    for apk in apkList:
        apkPath = os.path.join(path,apk)

        f = open(apkPath)

        count = 0
        for line in f.readlines():
            if ":" and ";" in line:
                count +=1

        apkname = apk.split(".")[0]
        cmd = "echo {0} {1} >> {2}".format(apkname,count,outputPath)
        os.system(cmd)

        csvname= outputPath.split("/")[-1].split(".")[0] + ".csv"

        cmd = "echo {0} >> {1}".format(count,csvname)
        os.system(cmd)

        print "we are handle with {0}".format(apkname)


calculateCFG(oriPath,orioutputPath)
calculateCFG(repPath,repoutputPath)

