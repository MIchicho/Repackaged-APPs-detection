#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho
# Date     :  2017-05-12
# running  :  python getSignature
# function :  parse the dex file and get the CFG signature
#             we should delete the ad libraries as much as possible

import os

jarPath = "/home/chicho/workspace/repackaged/tools/CFGScanDroid-master/target/CFGScanDroid.jar"

oriPath = "/home/chicho/workspace/repackaged/result/original/"

repPath = "/home/chicho/workspace/repackaged/result/repackaged/"

orioutPutPath = "/home/chicho/workspace/repackaged/DroidSIM/original/"

repoutPutPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged/"



def getCFGsignature(Path,outPutPath):
    
    apkList = os.listdir(Path)

    for apk in apkList:

        dexPath = os.path.join(Path,apk,"bin/classes/classes.dex")
    
        apkFile = apk + ".txt"
        outPutFilePath = os.path.join(outPutPath,apkFile)

        cmd = "java -jar {0} -d -f {1} >> {2}".format(jarPath,dexPath,outPutFilePath)
        os.system(cmd)

        tips = "handle with {0} ...".format(apkFile)
        print tips 



getCFGsignature(oriPath,orioutPutPath)
getCFGsignature(repPath,repoutPutPath)


print "all work is done!"




