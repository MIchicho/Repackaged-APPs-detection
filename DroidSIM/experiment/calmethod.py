#!/usr/bin/env python
# coding=utf-8
# Function  :  1. calculate the whole methods 
#              2. get the average number of methods 

import os


oripath = "/home/chicho/workspace/repackaged/DroidSIM/experiment/ori_nodelete_CFG.csv"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/experiment/rep_nodelete_CFG.csv"

orif = open(oripath)
repf = open(repPath)


lines = orif.readlines() + repf.readlines()

min = 100000
max = 0 

sum = 0.0 
avg = 0.0 
for line in lines:

    line = line.replace("\n","")
    line = int(line)

    if max < line:
        max = line 

    if min > line:
        min = line
    
    sum +=line 


avg = sum * 1.0/len(lines)

print max 
print min
print sum 
print avg 


