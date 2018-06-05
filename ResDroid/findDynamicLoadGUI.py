#!/usr/bin/env python
# coding=utf-8
import os
import sys

path=sys.argv[1]
out_path= "/home/chicho/result/APK3/"
if not os.path.exists(path):
    print "The path is not exists!"
    sys.exit(1)

fileList= os.listdir(path)

for filename in fileList:
    filePath = os.path.join(path,filename)
    resPath = os.path.join(filePath,"res")
    resList = os.listdir(resPath)
    flag = 0
    for L in resList:
        if L == "layout":
            flag = 1

    if flag == 0:
        print filename
       # cmd = "mv {0} {1}".format(filePath,out_path)
       # os.system(cmd)
        



