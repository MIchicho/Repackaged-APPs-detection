#!/usr/bin/env python
# coding=utf-8
import os

path = "/home/chicho/Workspace/ResDroid/experiment/kdtree/output.txt"

f = open(path,'r')

lineList = []

for line in f.readlines():
    line = line.replace("\r","")
    line = line.replace("\n","") 
    line=line.split(':')
    num=line[1]
    num = num.split(" ")
    cluster=num[1]
    if cluster != '1':
        cmd = "echo {0} >>kdtreeoutput.txt".format(cluster)
        os.system(cmd)


'''
for line in f.readlines():
    print line
    cmd = "./extractKD_cdf_hist.sh {0}".format(line)
    os.system(cmd)
'''

f.close()


print "all work done!\n"
