#!/usr/bin/env python
# coding=utf-8


import os 

oriPath = "/home/chicho/workspace/repackaged/ResDroid/original.txt"

repPath = "/home/chicho/workspace/repackaged/ResDroid/repackaged.txt"

orif = open(oriPath)
orilines = orif.readlines()
orif.close()

repf = open(repPath)
replines = repf.readlines()
repf.close()

lines = orilines + replines

a= [0]*18

j=0
for line in lines:
    line = line.replace("\n","")

    segs = line.split(",")

    for i in range(1,len(segs)):
        if segs[i] == '0':
            a[i-1] +=1 
    


    

print a 


print 'all work is done!'


