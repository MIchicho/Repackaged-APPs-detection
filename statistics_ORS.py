#!/usr/bin/env python
# coding=utf-8
# Author   : Chicho
# date     : 2017-3-11
# function : 1. find some rules among the date 
#            2. parse simipleResult.csv file and get how many app pairs 
#            has similarity is 99 sth like that 

import os 

path = "/home/chicho/workspace/repackaged/DroidMOSS/code/simpleResult.csv"

outputPath = "/home/chicho/workspace/repackaged/DroidMOSS/code/experiment/statisticsResult.csv"
f=open(path)

dict={}

for line in f.readlines():
    line = line.replace("\n","")
    similarValue = line.split(",")[2]
    smV = int(similarValue)

    if not dict.has_key(smV):
        dict[smV]=1
    else:
        dict[smV] += 1



# traverse the whole dict 
for key in dict:
    cmd = "echo {0},{1}>>{2}".format(key,dict[key],outputPath)
    os.system(cmd) 



print "all work is done!"

