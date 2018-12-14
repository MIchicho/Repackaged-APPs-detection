#!/usr/bin/env python
# coding=utf-8


import os 

path = "/home/chicho/workspace/repackaged/DroidMOSS/code/experiment/parseResult_OriRep.csv"

f = open(path)

for line in f.readlines():

    line = line.replace("\n","")

    sha_ori = line.split(",")[1]

    sha_rep = line.split(",")[3]

    simValue = line.split(",")[4]

    cmd = "echo {0},{1}>> pair2.txt".format(sha_ori,sha_rep)
    os.system(cmd)



print "all work is done!"
