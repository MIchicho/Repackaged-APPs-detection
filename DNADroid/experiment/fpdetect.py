#!/usr/bin/env python
# coding=utf-8
# Author   :   Chicho
# date     :   2017-07-07 
# function :   1.get the false negative of DNADroid who has not ad libs


import os 

path = "/home/chicho/workspace/repackaged/DNADroid/filter/similarScore.csv"

f =open(path)

lineList = f.readlines()

def getfnegative(lines):
    
    fnCnt = 0

    for line in lineList:
        line = line.replace("\n","")
        
        segs = line.split(",")

        data1 = float(segs[2])
        data2 = float(segs[3])

        tmp = max(data1,data2)

        if tmp < 0.7:
            fnCnt += 1
            print fnCnt
            print line 
            cmd = "echo {0} >> {1} ".format(line,"falseNegative.txt")
            os.system(cmd)




getfnegative(lineList)

print "all work is done!"
