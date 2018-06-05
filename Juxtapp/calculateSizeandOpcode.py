#!/usr/bin/env python
# coding=utf-8
'''
@  Author   :  Chicho
@  Date     :  2017-05-05
@  function :  calculate the Ground truth apps' size and total number
               of the opcodes
'''

import os

oriApkPath = "/home/chicho/workspace/repackaged/pairs/original/"

repApkPath = "/home/chicho/workspace/repackaged/pairs/repackaging/"

oriInsPath = "/home/chicho/workspace/repackaged/Juxtapp/original/"

repInsPath = "/home/chicho/workspace/repackaged/Juxtapp/repackaged/"


oriAPKList = os.listdir(oriApkPath)
repAPKList = os.listdir(repApkPath)

oriInsList = os.listdir(oriInsPath)
repInsPath = os.listdir(repInsPath)


def calculate_Size(list):

    sumSize = 0
    for apk in list:
        apkPath = os.path.join(oriApkPath,apk)

        size = os.path.getsize(apkPath)

        sumSize += size

    return sumSize


# original size 

oriAPKSize = calculate_Size(oriAPKList)
repAPKSize = calculate_Size(repAPKList)

cmd = "echo {0} >> {1}".format()

