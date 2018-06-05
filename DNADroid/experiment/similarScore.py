#!/usr/bin/env python
# coding=utf-8

import os 
import networkx as nx
from networkx.algorithms import isomorphism
import time 
import sys

oriPath = "/home/chicho/workspace/repackaged/DNADroid/filter/original/"

repPath = "/home/chicho/workspace/repackaged/DNADroid/filter/repackaged/"

pairPath = "/home/chicho/workspace/repackaged/DNADroid/experiment/cluster/cluster6"

origraph = "/home/chicho/workspace/repackaged/DNADroid/filter/graph/original/"

repgraph = "/home/chicho/workspace/repackaged/DNADroid/filter/graph/repackaged/"


def createGraph(lines):

    GNameList = []
    GL = []
    
    for line in lines:

        if ":" and ";" in line:
            line = line.replace("\n","")

            segs = line.split(";")

            graphName = segs[0] 
        
            GNameList.append(graphName)
            

            G = nx.DiGraph()

            for i in range(2,len(segs)):

                if "," not in segs[i] and ":" in segs[i]:
                    edges = segs[i].split(":")

                    G.add_edge(int(edges[0]),int(edges[1]))


                if ":" in segs[i] and "," in segs[i]:
                    items = segs[i].split(":")        # 0:1,2 

                    edges = items[1].split(",")

                    for index in range(len(edges)):

                        G.add_edge(int(items[0]),int(edges[index]))

            GL.append(G)


    return (GNameList,GL)
            

# invoke last invoke 
def parseSig(oriPath,repPath):

    f = open(pairPath)
    
#    i = 0
    apkList = []

    for line in f.readlines():
        
        line = line.replace("\n","")
        apks = line.split(",")

        oriapk = apks[0] + ".txt"
        repapk = apks[1] + ".txt"

        oriAPKPath = os.path.join(oriPath,oriapk)
        repAPKPath = os.path.join(repPath,repapk)

        if not os.path.exists(oriAPKPath) and os.path.exists(repAPKPath):
            cmd = "echo {0} >> {1}".format(apks[0],"orinoexists")
            os.system(cmd)
            continue
        if not os.path.exists(repAPKPath) and os.path.exists(oriAPKPath):
            cmd = "echo {0} >> {1}".format(apks[1],"repnoexists")
            os.system(cmd)
            continue 
        if not os.path.exists(repAPKPath) and not os.path.exists(oriAPKPath):
            cmd = "echo {0},{1} >> {2}".format(apks[0],apks[1],"noexists")
            os.system(cmd)
            continue

        if not oriAPKPath in apkList:
            apkList.append(oriAPKPath)

        if not repAPKPath in apkList:
            apkList.append(repAPKPath)
        
        print "we are here!"
        print apkList

    for oriapk in apkList:

        for repapk in apkList:

            if oriapk == repapk:
                continue 
 
            if os.path.exists(oriapk) and os.path.exists(repapk):
                orif = open(oriapk)
                repf = open(repapk)
                tips = "compare the apk pairs {0},{1}".format(oriapk.split("/")[-1],repapk.split("/")[-1])
                print tips 
            else:
                continue

            orifLines = orif.readlines()
            repfLines = repf.readlines()

            oriGNameList,OGL = createGraph(orifLines)
            repGNameList,RGL = createGraph(repfLines)

            if len(OGL)==0 or len(RGL)==0:
                continue

            tips = "the number of Graphs in original {0}".format(len(OGL))
            print tips 

            tips = "the number of Graph in repackaged {0}".format(len(RGL))
            print tips 
        
            mCnt = 0
            start1 = time.time()

            for GName in oriGNameList:

                if GName in repGNameList:
                   # print GName 
                    Gindex = oriGNameList.index(GName)
                    Tindex = repGNameList.index(GName)

                    G = OGL[Gindex]
                    T = RGL[Tindex]

                    GM = isomorphism.DiGraphMatcher(G,T)

                    if GM.subgraph_is_isomorphic():
                        print GM.mapping
                        mCnt += 1

            if len(oriGNameList):
                SimA_b = mCnt*1.0/len(oriGNameList)
                print SimA_b
            else:
                SimA_b =0
        
            end1 = time.time()

            elpase1 = end1-start1


            start2 = time.time()
            mCnt = 0
            for TName in repGNameList:

                if TName in oriGNameList:
                    print TName
                    Tindex = repGNameList.index(TName)
                    Gindex = oriGNameList.index(TName)

                    G = OGL[Gindex]
                    T = RGL[Tindex]

                    GM = isomorphism.DiGraphMatcher(T,G)

                    if GM.subgraph_is_isomorphic():
                       # print GM.mapping
                        mCnt += 1

            if len(repGNameList)!=0:
                SimB_a = mCnt*1.0/len(repGNameList)

            else:
                SimB_a = 0

            end2 = time.time()
            elpase2 = end2 - start2

            # ***********************************

            cmd = "echo '{0}','{1}',{2},{3} >>{4}".format(oriapk.split("/")[-1].split(".")[0],repapk.split("/")[-1].split(".")[0],SimA_b,SimB_a,"similarScore6.csv")
            os.system(cmd)

            cmd = "echo {0} >> {1}".format(SimA_b,"ori_repSimilarValue4.csv")
    #        os.system(cmd)
            cmd = "echo {0} >> {1}".format(SimB_a,"rep_oriSimilarValue4.csv")
   #         os.system(cmd)

            cmd1 = "echo {0},{1},{2},{3} >> {4}".format(oriapk.split("/")[-1].split(".")[0],repapk.split("/")[-1].split(".")[0],elpase1,elpase2,"runningtime.txt")
  #          os.system(cmd1)

            cmd2 = "echo {0} >> {1}".format(elpase1,"orirunningTime4.csv")
 #           os.system(cmd2)

            cmd3 = "echo {0} >>{1}".format(elpase2,"reprunningTime4.csv")
#            os.system(cmd3)




        


parseSig(oriPath,repPath)


print "all work is done!"




