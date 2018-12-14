#!/usr/bin/env python
# coding=utf-8
# author   :  Chicho
# date     :  2018-05-09
# function :  This file is parse the file in filter directory similarScore.csv and get the larger score  

import os 


simPath ="/home/chicho/workspace/repackaged/DNADroid/filter/similarScore.csv"

f=open(simPath)
lines = f.readlines()

f.close()

for line in lines:
    line = line.replace("/n","")

    segs = line.split(",")

    sim1 = float(segs[2])
    sim2 = float (segs[3])

    maxValue = max(sim1,sim2)

    cmd = "echo {0}>> {1}".format(maxValue,"largeScore.csv")
    os.system(cmd)


print "all work is done!"
