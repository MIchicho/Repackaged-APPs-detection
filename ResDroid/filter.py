#!/usr/bin/env python
# coding=utf-8

import os 


print'''
=======================
input -> 0 : strict 
input -> 1 : corase
=======================
'''


input = raw_input("your choice? 0 or 1?")


if input == '0':
    path = "/home/chicho/workspace/repackaged/ResDroid/Strict_similarScore"

if input == '1':
    path = "/home/chicho/workspace/repackaged/ResDroid/Corase_similarScore"

f=open(path)

lines = f.readlines()

for line in lines:
    line = line.replace("\n","")

    segs = line.split(",")

    sim = float(segs[2])

    if sim >=1 and input =='0':
        cmd = "echo {0} >> {1}".format(line,"strictfliter.txt")
        os.system(cmd)
    elif sim>1 and input == '1':
        cmd = "echo {0} >>{1}".format(line,"Corasefilter.txt")
        os.system(cmd)


print "all work is done!"
