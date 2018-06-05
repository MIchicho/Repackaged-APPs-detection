#!/usr/bin/env python
# coding=utf-8
# Author   : Chicho 
# running  : python getCaseStudy.py 
# Date     : 2017-07-24 
# function : 1.parse the similarScore.txt file and get the similarity score 
#              which is less than 0.7 
#            2. store these app pairs into caseStudy.txt file 

import os 

path = "/home/chicho/workspace/repackaged/ViewDroid/experiment/casestudy/similarScore.txt"


f = open(path)

lines = f.readlines()

for line in lines:
    line = line.replace("\n","")

    segs = line.split(",")

    simScore = float(segs[2])

    if simScore < 0.7:
        cmd = "echo {0} >>{1}".format(line,"caseStudy.txt")
        os.system(cmd)


print "all work is done!"


