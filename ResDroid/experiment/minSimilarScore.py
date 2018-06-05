#!/usr/bin/env python
# coding=utf-8

#  function : parse the file  Strict_similar.csv  and get the similar value

import os 

simPath = "/home/chicho/workspace/repackaged/ResDroid/similarScore/Strict_similarScore.csv"

f =open(simPath)

lines = f.readlines()

for line in lines:
    line = line.replace("\n","")

    segs = line.split(",")

    sim1 = float(segs[2])

    sim2 = float(segs[3])

    minValue = min(sim1,sim2)
    
    cmd = "echo {0}>>{1}".format(minValue,"minSimValue.csv")
    os.system(cmd)


print "all work is done!"
