#!/usr/bin/env python
# coding=utf-8
import os

path="/home/chicho/Workspace/ResDroid/experiment/kdtree/KDOutput.txt"


f=open(path,'r')

i = 0
nns_res=[]
nns_len = len(nns_res)
for line in f.readlines():
    line = line.replace("\n","")
    res = line.split(":")
    num = res[0]
    

    if nns_res == []:
        nns_res.append(0)
        per = num 
     

    if num == per:
        nns_res[i] += 1
        
    else:
        i +=1
        nns_res.append(1)
        per = num
     

f.close()


nns_len=len(nns_res)

for i in range(nns_len):
    cmd = "echo {0}:{1}>>kdresult.txt".format(i, nns_res[i])
    os.system(cmd)



    
