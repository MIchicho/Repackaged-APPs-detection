#!/usr/bin/env python
# coding=utf-8
import os

path = "/home/chicho/Workspace/ResDroid/experiment/20E-4-60k-test-data.txt"

f =  open(path,'r')

for line in f.readlines():
    line = line.replace("\n",'')
    cmd = "./extractData.sh '{0}'".format(line)
    os.system(cmd)

    cmd = "insert {0}".format(line)
    os.system(cmd)


print "all work done!\n"    
