#!/usr/bin/env python
# coding=utf-8
#  Author   :  Chicho
#  Date     :  2017-08-16 
#  Running  :  python findChangeVector.py 
#  function :  1. compare the original apps and repackaged apps and find the different vector 
#              2. store the original app's and repackaged app's vector into a list and compare the similarity 
#              3. we should count the number of how many app pairs are different 
#              4. we also should find which features change most
#              5. the changed number 


import os 

oriPath = "/home/chicho/workspace/repackaged/ResDroid/original.txt"

repPath = "/home/chicho/workspace/repackaged/ResDroid/repackaged.txt"

pairPath = "/home/chicho/workspace/repackaged/ResDroid/repackaging_pairs.txt"

oriDict = {}

repDict = {}

def createDict(lines,appDict):
    
    for line in lines:
        line = line.replace("\n","")
        segs = line.split(",")

        apkname = segs[0]

        apkVec = segs[1:]

        if apkname not in appDict.keys():
            appDict[apkname]=apkVec

    return appDict 

orif = open(oriPath)
orifLines = orif.readlines()
orif.close()

repf = open(repPath)
repLines = repf.readlines()
repf.close()

oriDict = createDict(orifLines,oriDict)
repDict = createDict(repLines,repDict)

def findDiff(oriDict,repDict):

    f =open(pairPath)
    lines = f.readlines()

    fn = [0]*18
    fc = [0]*18 
    count = 0 
    for line in lines:
        line = line.replace("\n","")
        segs = line.split(",")

        oriapk = segs[0]
        repapk = segs[1]
        
        if oriapk in oriDict.keys() and repapk in repDict.keys():
            oriVec = map(int,oriDict[oriapk])
            repVec = map(int,repDict[repapk])
        else:
            continue

        if oriVec != repVec:
            count += 1
            for i in range(len(oriVec)):
                if oriVec[i]!=repVec[i]:
                    fn[i] += 1
                    fc[i] += abs(oriVec[i]-repVec[i])


    cmd = "echo count: {0} >> {1}".format(count,"result")
    os.system(cmd)

    cmd = "echo {0} >> {1}".format(fn,"result")
    os.system(cmd)

    cmd = "echo {0} >> {1}".format(fc,"result")
    os.system(cmd)

    print count 
    print fn 
    print fc 
    
    c = [0]*18 
    for i in range(len(fn)):
        if fn !=0:
            c[i] = fc[i]/fn[i]


    print c


findDiff(oriDict,repDict)



print "all work is done!"
