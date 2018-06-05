#!/usr/bin/env python
# coding=utf-8

import os 
import time 

print "Usage:"

print '''
=======================================================
running : python mJaccard.py
You can input different number to choose different path
*******************************************************
input : 0 -> original1 path 
input : 1 -> app delete ads
input : 2 -> test path 
=======================================================
'''


pairPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaging_pairs.txt"

input = raw_input("you choice? 0 or 1 or 2:\n")

while(input!='0') and (input != '1') and (input!='2'):
    print "your input is wrong!"
    input = raw_input("your choice? 0 or 1 or 2:\n")

if (input == '0'):
    oriPath = "/home/chicho/workspace/repackaged/DroidSIM/original/"
    repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged/"
    outputPath = "/home/chicho/workspace/repackaged/MassVet/3D-CFG/mcoreSimilar.csv"

if (input == '1'):
    oriPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/original1/"
    repPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/repackaged1/"
    outputPath = "/home/chicho/workspace/repackaged/MassVet/3D-CFG/deleteAdssimila"
if (input == '2'):
    oriPath = "/home/chicho/workspace/repackaged/DroidSIM/original"
    repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged/"
    
    outputPath = "/home/chicho/workspace/repackaged/MassVet/3D-CFG/test/similar.csv"

    pairPath = "/home/chicho/workspace/repackaged/MassVet/3D-CFG/test/pair.txt"
    

def calJaccard():

    f= open(pairPath)

    lines = f.readlines()

    for line in lines:
        line = line.replace("\n","")
        segs = line.split(",")

        oriapkfile = segs[0]
        repapkfile = segs[1]

        oriapk = segs[0] + ".txt"
        repapk = segs[1] + ".txt"

        oriapkPath = os.path.join(oriPath,oriapk)

        repapkPath = os.path.join(repPath,repapk)

        try:
            orif = open(oriapkPath)

            repf = open(repapkPath)
        except:
            
            continue 

        oriflines = orif.readlines()

        repflines = repf.readlines()
        
        orilineList = []
        repLineList = []

        oriList = []
        repList = []

        for line in oriflines:
            line = line.replace("\n","")
            orilineList.append(line)

            segs = line.split(";")
            
            del segs[0]

            newline = ";".join(segs)
            oriList.append(newline)

        for line in repflines:
            line = line.replace("\n","")
            repLineList.append(line)

            segs = line.split(";")

            del segs[0]

            newline = ";".join(segs)
            repList.append(newline)
        
        inter = 0.0
#        Inter = 0.0 
        union = 0.0 
#        Union = 0.0

        

    



        if len(oriList)< len(repList):

            for ori in oriList:
                if ori in repList:
                    
                    inter += 1
                    

            union = len(repList) + len(oriList) - inter 

        else:

            for rep in repList:
                if rep in oriList:
                    inter += 1

            union = len(repList) + len(oriList) - inter  

        jaccard = inter/union 

        cmd = "echo {0},{1},{2}>>{3}".format(oriapkfile,repapkfile,jaccard,outputPath)
        os.system(cmd)

        '''
        if len(oriList) < len(repList):

            for i in range(len(oriList)):
                if orilineList[i] == repLineList[i]:
                    inter += 1
                    Inter += 1
                    union += 1
                    Union += 1
                    continue
                if orilineList[i]!=repLineList[i] and oriList[i]!=repList[i]:
                    inter += 1
                    union += 1
                    continue 

        '''   

start = time.time()
calJaccard()

end = time.time()

elapse = end- start

cmd = "echo {0}>>{1}".format(elapse,"similarTime")
os.system(cmd)
