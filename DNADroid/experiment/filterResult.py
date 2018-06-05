#!/usr/bin/env python
# coding=utf-8
# author   :  Chicho
# running  :  python filterResult.py
# function :  analyze the similiarScore.csv file and we find two apps whose similar 
#             Score is larger than 0.7 

import os 


path = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/similarScore.csv"

oripath = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/apk_pairs"

f = open(path)

lines = f.readlines()
lineList = []

for line in lines:
    line = line.replace("\n","")
    segs = line.split(",")

    sim1 = float(segs[2])
    sim2 = float(segs[3])

    maxsim = max(sim1,sim2)

    if maxsim>=0.7:
        cmd = "echo {0} >>{1}".format(line,"filterScore")
        os.system(cmd)

        cmd = "echo {0},{1} >> {2}".format(segs[0],segs[1],"filter_Pairs")
        os.system(cmd)

        newline = segs[0]+","+segs[1]
        lineList.append(newline)

        print line 


print "all work is done!"


orif = open(oripath)
orifLines = orif.readlines()
orifList = [] 

for line in orifLines:
    line = line.replace("\n","")
    segs = line.split(",")
    newline = segs[0]+","+segs[1]
    orifList =  orifList.append(newline)

print "*********************"
for line in orifList:
    if not line in lineList:
        print line 
        cmd = "echo {0} >>{1}".format(line,"notfind")
        os.system(cmd)


print "all work is done!"


