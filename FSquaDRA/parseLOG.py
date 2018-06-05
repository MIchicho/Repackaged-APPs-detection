#!/usr/bin/env python
# coding=utf-8
#  @author   : Chicho
#  @date     : 2018-04-14
#  @function : 1.parse the LOG file and get the comparing time 
#              2. get apk attribute to memeory 
import os 

logPath = "/home/chicho/workspace/repackaged/FSquaDRA/LOG"

f=open(logPath)
lines = f.readlines()

for line in lines:
    line = line.replace("\n","")
    if line.startswith("Getting apk attributes to memory took"):
        segs =line.split(":")
        time = segs[1]
        cmd = "echo {0} >>{1}".format(time,"processTime")
        os.system(cmd)

    if line.startswith("Comparing apk attributes took"):
        segs =line.split(":")
        time = segs[1]
        cmd = "echo {0} >>{1}".format(time,"comparingTime")
        os.system(cmd)


print "all work is done!"
