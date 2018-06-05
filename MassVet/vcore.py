#!/usr/bin/env python
# coding=utf-8
# Author    :  Chicho 
# Date      :  2017-10-03 
# filename  :  vcore.py 
# running   :  python vcore.py 
# function  :  1. parse the a3e and get the active weight; all the widgets is the weight of its node 
#              2. calculate the weight for the activity node 
#              3. we get the ATG 
#              4. calculate the vcore 



import networkx as nx 
import numpy as np 
import os
import xml.dom.minidom
import time 


print "Usage:"

print '''
===============================================================
running : python mcore.py 
you can input different number to choose the different path
***************************************************************
input : 0 -> original APKs
input : 1 -> repackaged APKs 
input : 2 -> test path 
===============================================================
'''

print "\n"


input = raw_input("your choice? 0 or 1 or 2:\n")


while (input != '0') and (input !='1') and (input != '2'):
    print "your input is wrong!"
    input = raw_input("you choice? 0 or 1 or 2:\n")



if (input == '0'):
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/"
    weightPath = "/home/chicho/workspace/repackaged/MassVet/UIWeight/original/"
    graphPath = "/home/chicho/workspace/repackaged/MassVet/graph/original/"


if (input == '1'):
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/"
    weightPath = "/home/chicho/workspace/repackaged/MassVet/UIWeight/repackaged/"
    graphPath = "/home/chicho/workspace/repackaged/MassVet/graph/repackaged/"


if (input == '2'):
    satgPath = "/home/chicho/test/problem_Test/satg/"
    weightPath = "/home/chicho/test/problem_Test/UIWeight"
    graphPath = "/home/chicho/test/problem_Test/graph/"





if not os.path.exists(weightPath):
    os.makedirs(weightPath)


def parseWeight(eachsatgPath,weightPath):

    print "we are in the parseWeight"


    try:
        dom = xml.dom.minidom.parse(eachsatgPath)
    except:
        return 

    root = dom.documentElement

    parentActList = root.getElementsByTagName('Activity')

    parentActNameCollection = []

    weightDict = {}

    for activity in parentActList:
        parentName = activity.getAttribute('name')

        #delete the ads
        if parentName.startswith('com.google.ads'):
            continue 

        if parentName.startswith('com.admob.android'):
            continue 

        if parentName.startswith('com.umeng'):
            continue

        if parentName.startswith('com.inmobi'):
            continue 

        if parentName.startswith('com.yume'):
            continue

        if parentName.startswith('com.kiwi.ads'):
            continue 

        if parentName.startswith('com.pontiflex'):
            continue 

        if parentName.startswith('com.adsdk'):
            continue

        if parentName.startswith('com.gfan.sdk'):
            continue 

        if parentName.startswith('com.facebook'):
            continue

        if not parentName in parentActNameCollection:
            parentActNameCollection.append(parentName)


        childActList = activity.getElementsByTagName('ChildActivity')

        if not parentName in weightDict.keys():
            weightDict[parentName] = len(childActList)



    return weightDict





#**********************************************************************
#**********************************************************************

def createGraph(lines):

    GL = []

    i = 0

    while(i<len(lines)):
        line = lines[i]

        if " " not in line:
            Gname = line.replace("\n","")

            Gname = nx.MultiDiGraph()

            i = i + 1 

            line = lines[i]

            while ((" " in line) and (i < len(lines))):
                line = line.replace("\n","")
                edge = line.split(" ")
                Gname.add_edge(edge[0],edge[1])
                
                i = i + 1

                if i < len(lines):
                    line = lines[i]


        if Gname not in GL:
            GL.append(Gname)


    return GL 




def readFile(GPath):

    fileList = os.listdir(GPath)

    for file in fileList:
        print file 
        satg = file + ".apk.g.xml"
        eachsatgPath = os.path.join(satgPath,satg)

        weightDict = parseWeight(eachsatgPath,weightPath)

        print "the weight of each node:"

        print weightDict 
        

        print "++++++++++++++++"

        fPath = os.path.join(GPath,file)
        f = open(fPath)

        lines = f.readlines()

        GL = createGraph(lines)

    

        if len(GL)!=0:

            for G in GL:
                print "*************************************" 
                indexNo = GL.index(G)
                cmd = "graph{0}".format(indexNo)
                print cmd 

                print "graph edges"
                print G.edges()
                

                if len(G.edges())<3:
                    continue 

                outDegreeDict = G.out_degree()
                cycleList = list(nx.simple_cycles(G))
                VectorDict = {}
                dfsNodeList = list(nx.dfs_preorder_nodes(G))# 深度遍历节点的先后顺序
                
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
                        VectorDict[dfsNodeList[i]]= eachNode
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


                # calculate the vcore 
                
                factor = np.zeros(3)
                weight = 0.0 

                for edge in G.edges():
                    node1 = edge[0]
                    node2 = edge[1]

                    if node1 in weightDict.keys():
                        weight1 = weightDict[node1]
                    else:
                        weight1 = 0 

                    if node2 in weightDict.keys():
                        weight2 = weightDict[node2]
                    else:
                        weight2 = 0
                    
                    factor += np.array(VectorDict[node1])*weight1 + np.array(VectorDict[node2])*weight2

                    weight = weight + weight1 + weight2 
                

                print "factor"
                print factor

                if weight==0:
                    continue

                factor = factor/weight 

                print "***factor****"

                print factor 
                
                if (factor==np.zeros(3)).all():
                    print "the centroid is 0!"
                    continue

            

                cmd = "echo {0},{1}>>{2}".format(file,factor,"vcore_one_weight.csv")
          #      os.system(cmd)


                cmd = "echo {0},{1},{2},{3}>>{4}".format(file,factor[0],factor[1],factor[2],"vcoreDetail_one_weight.csv")
            #    os.system(cmd)
                
               # break   we just need one graph 
                break
    
readFile(graphPath)
