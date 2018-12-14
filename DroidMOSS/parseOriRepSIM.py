#!/usr/bin/env python
# coding=utf-8
# Author   : Chicho 
# date     : 2017-3-11
# running  : python parseOriRepSIM.py path_file_you_needparse
# function : 1. we use the calOriRepfrpair.py get the OriRep_result.txt
#            file and store them into the experiment directory 
#            2. we use this file parse the OriRep_result.txt and get the 
#            parseResult_OriRep.csv file
#            3. we need to draw a picture 
# pay attention to I need to finish the writing this night 

import os 
import sys 

if len(sys.argv) == 2:
    fileName = sys.argv[1]
else:
    sys.exit()

path = "/home/chicho/workspace/repackaged/DroidMOSS/code/"

output = "/home/chicho/workspace/repackaged/DroidMOSS/code/experiment/"

filePath = os.path.join(path,fileName)
fileNamePrefix = fileName.split(".")[0] 
outFileName = "parse_" + fileNamePrefix + ".csv"

outputPath = os.path.join(output,outFileName)
simpleFile = "simple_"+fileNamePrefix + ".csv"
simpleOutPutPath = os.path.join(output,simpleFile)

f = open(filePath)

for line in f.readlines():
    arr1 = line.split()[0]
    arr2 = line.split()[2]
    arr3 = line.split()[3]

    class1 = arr1.split("/")[-2]
    sha1 = arr1.split("/")[-1].split(".")[0]

    class2 = arr2.split("/")[-2]
    sha2 = arr2.split("/")[-1].split(".")[0]

    similarValue = arr3.split("(")[1].split(")")[0]

    cmd = "echo {0},{1},{2},{3},{4}>>{5}".format(class2,sha2,class1,sha1,similarValue,outputPath)
    os.system(cmd)

    cmd = "echo {0},{1},{2}>>{3}".format(sha2,sha1,similarValue,simpleOutPutPath)
    os.system(cmd)

    tips = "{0} {1} {2}".format(sha2,sha1,similarValue)
    print tips 



f.close()

print "all work is done!"

