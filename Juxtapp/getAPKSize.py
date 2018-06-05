#!/usr/bin/env python
# coding=utf-8
#  Author   :  Chicho
#  running  :  pyhton getAPKSize.py
#  function :  get the size of APK file and use this data to draw the 
#              experiment figure 

import os

oriPath = "/home/chicho/workspace/repackaged/pairs/original/"

repPath = "/home/chicho/workspace/repackaged/pairs/repackaging/"

oriList = os.listdir(oriPath)
repList = os.listdir(repPath)

maxAPK=""
maxSize=0
minAPK = ""
minSize = 0


for apk in oriList:
    apkPath = os.path.join(oriPath,apk)
    apkSize = os.path.getsize(apkPath)

    if apkSize > maxSize:
        maxSize = apkSize
        maxAPK = apk 

    if apk == oriList[0]:
        minAPK = apk 
        minSize = apkSize
    elif minSize > apkSize:
        minSize = apkSize
        minAPK = apk 

    cmd = "echo {0} >> {1}".format(apkSize,"originalSize.csv")
    os.system(cmd)

line = "{0},{1}".format(maxAPK,maxSize)
print line 

line1 = "{0},{1}".format(minAPK,minSize)
print line1


maxAPK=""
maxSize = 0
minAPK = ""
minSize = 0

for apk in repList:
    apkPath = os.path.join(repPath,apk)
    apkSize = os.path.getsize(apkPath)

    if apkSize > maxSize:
        maxSize = apkSize
        maxAPK = apk 


    if apk == repList[0]:
        minAPK = apk
        minSize = apkSize
    elif minSize > apkSize:
        minSize = apkSize
        minAPK = apk

    cmd = "echo {0} >> {1}".format(apkSize, "repackagedSize.csv")
    os.system(cmd)

line = "{0},{1}".format(maxAPK,maxSize)
print line 

line1 = "{0},{1}".format(minAPK,minSize)
print line1


print "all Work is done!"


