#!/usr/bin/env python
# coding=utf-8
# Author   :   Chicho
# Date     :   2018-01-31
# FileName :   mcore.py
# Function :   1. parse the graph and get the centroid for each method

import networkx as nx
import numpy as np 
import os
import time

print "Usage:"

print '''
=========================================================
running : python mcore.py
You can input different number to choose different path 
*********************************************************
input  : 0 -> original APKs
input  : 1 -> repackaged APKs
input  : 2 -> test path 
=========================================================
'''


print "\n"


input = raw_input("Your choice? 0 or 1 or 2:\n")

while (input != '0') and (input !='1') and (input != '2'):
    print "your input is wrong!"
    input = raw_input("your choice? 0 or 1 or 2:\n")


if (input == '0'):
    graphPath = "/home/chicho/workspace/repackaged/DroidSIM/original/"
    outputPath = "/home/chicho/workspace/repackaged/MassVet/3D-CFG/original/"


if (input == '1'):
    graphPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged/"

    outputPath = "/home/chicho/workspace/repackaged/MassVet/3D-CFG/repackaged/"

if (input =='2'):
    graphPath = "/home/chicho/workspace/repackaged/DroidSIM/test/"

    outputPath = "/home/chicho/workspace/repackaged/MassVet/3D-CFG/test/"



#********************************************************************
# parse the graph and create the graph for calculating the centroid 
#******************************************************************** 

def parseCreateGraph(lines):

    GL = []

    i = 0

    while (i < len(lines)):
        line = lines[i]

        if " " not in line:
            G = nx.DiGraph()  # 注意我们需要创建一个有向图

            i = i + 1

            line = lines[i]  # 往下移动，得到这个图的第一条bian

            while ((" " in line) and (i < len(lines))):
                line = line.replace("\n","")
                edge = line.split(" ")
                G.add_edge(edge[0],edge[1])

                i = i + 1 

                if i < len(lines):
                    line = lines[i]

        if G not in GL:
            GL.append(G)


    return GL 



#***************************************
#  read the graph and output the result 
#***************************************


def readFile(Gpath):

    fileList =  os.listdir(Gpath)  # get the graph and parse the result 

    for file in fileList:
        print file 
        
        filePath = os.path.join(Gpath,file)

        f = open(filePath)

        lines = f.readlines()

        GL = parseCreateGraph(lines)

        outputFilePath = os.path.join(outputPath,file)

        if len(GL)!=0:
            
            for G in GL:
                print "*******************************"
                indexNo = GL.index(G)
                cmd = "graph{0}".format(indexNo)
                print cmd 

                print "graph edges"
                print G.edges()

                
                outDegreeDict = G.out_degree()
                cycleList = list(nx.simple_cycles(G))
                VectorDict = {}
                dfsNodeList = list(nx.dfs_preorder_nodes(G))   #

                print "dfsNodeList"
                print dfsNodeList
                print "cycleList"
                print cycleList
                print "outDegreeDict"
                print outDegreeDict 

                eachNode = []

                for i in range(len(dfsNodeList)):
                    eachNode.append(i)

                    if dfsNodeList[i] not in VectorDict.keys():
                        VectorDict[dfsNodeList[i]] = eachNode 
                        eachNode = []

                print "VectorDict"
                print VectorDict 

                for key in outDegreeDict.keys():
                    eachNode = VectorDict[key]
                    eachNode.append(outDegreeDict[key])
                    eachNode.append(0)
                    VectorDict[key]=eachNode 


                print "VectorDict"
                print VectorDict 

                if len(cycleList)!=0:
                    for cycle in cycleList:
                        for ele in cycle:
                            eachNode = VectorDict[ele]
                            eachNode[2] += 1
                            VectorDict[ele] = eachNode 

                print "VectorDict"
                print VectorDict  

                for key in VectorDict.keys():
                    vector = VectorDict[key]
                    cmd = "echo {0}>>{1}".format(vector,outputFilePath)
                    os.system(cmd)



start = time.time()
readFile(graphPath)
end = time.time()

elpase = end-start 

cmd = "echo {0} >>{1}".format("the time for calculating the centroid for the apps","centroidTime")
os.system(cmd)
cmd = "echo {0} >>{1}".format(elpase,"centroidTime")
os.system(cmd)



