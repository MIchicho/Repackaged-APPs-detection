#!/usr/bin/env python
# coding=utf-8
#  Author   : Chicho
#  filename : Vf2.py
#  Function : parse the graph file 
#             the file format 
#             t1
#             0 1
#             0 2
#             1 3
#             1 4
#             create the graph according to the graph signature file 
#             compare the similarity and get the result

import os
import networkx as nx 
from networkx.algorithms import isomorphism 
import time 
import sys

oriGPath = "/home/chicho/workspace/repackaged/DroidSIM/graph/original/"

repGpath = "/home/chicho/workspace/repackaged/DroidSIM/graph/repackaged/"

pairPath = "/home/chicho/workspace/repackaged/repackaging_pairs1.txt"


# create the file 
def createGraph(lines):
    GL = []

    i = 0 

    while(i < len(lines)):

        line = lines[i]

        if " " not in line: # we find the graph name 
            Gname = line.replace("\n","")

            Gname = nx.Graph()   # create a graph 

            i = i + 1

            line = lines[i]

            while ((" " in line) and (i < len(lines))):
                line = line.replace("\n","")
                edge = line.split(" ")
                Gname.add_edge(int(edge[0]),int(edge[1]))
                i = i + 1

                if i < len(lines):
                    line = lines[i]

        if Gname not in GL:
            GL.append(Gname)

    return GL 


'''
def getcomparePair(pairPath):
    f=open(pairPath)

    for line in f.readlines():
        line = line.replace("\n","")

        apks = line.split(",")
'''

 

def VF(oriGPath,repGpath):
    
    f = open(pairPath)

    for line in f.readlines():
        line = line.replace("\n","")
        apks = line.split(",")
        
        oriapk = apks[0] + ".txt"
        repapk = apks[1] + ".txt"

        tips = "compare the apk pairs {0},{1}".format(apks[0],apks[1])
        print tips 

        oriAPKPath = os.path.join(oriGPath,oriapk)
        repAPKPath = os.path.join(repGpath,repapk)

        
        if os.path.exists(oriAPKPath) and os.path.exists(repAPKPath):
            orif = open(oriAPKPath)
            tarf = open(repAPKPath)
        else:
            if not os.path.exists(oriAPKPath) and os.path.exists(repAPKPath):
                cmd = "echo {0} >> {1}".format(apks[0],"noexists.txt")
                os.system(cmd)
            if not os.path.exists(repAPKPath) and os.path.exists(oriAPKPath):
                cmd = "echo {0} >> {1}".format(apks[1],"noexists.txt")
                os.system(cmd)
            if not os.path.exists(oriAPKPath) and not os.path.exists(repAPKPath):
                cmd = "echo {0},{1}>>{2}".format(apks[0],apks[1],"noexists.txt")
                os.system(cmd)

            continue 


        GG = createGraph(orif.readlines()) # which is an original apks and GG is all of CFG
        TG = createGraph(tarf.readlines()) # repackaged apks's CFGs

        start = time.time()
        
        b = 0
        for G in GG:

            for T in TG:

                GM = isomorphism.GraphMatcher(G,T)
                #GM1 = isomorphism.GraphMatcher(T,G)
                
                elapse = time.time() -start
                if int(elapse)>600:
                    break 

                if GM.subgraph_is_isomorphic():
                   # tips = "Graph {0} and {1} are isomorphic".format(G,T)
                   # print tips 
                    b = b + 1
                   # print GM.mapping
                    break
                else:
                    pass 
                   # print "There are not match"

                elapse = time.time() - start

                if int(elapse)>3600:
                    print "**************************"
                    print "Time is up!"
                    print "**************************"
                    break 

            
            nowtime = time.time()
            continueTime = nowtime - start

            if int(continueTime) >3600:
                continue 


        end = time.time()

        time_interval = str(end-start)

        cmd = "echo {0} >> {1}".format(time_interval,"runningtime.txt")
        os.system(cmd)
        
        if b > min(len(GG),len(TG)):
            sim = (b * 1.0)/max(len(GG),len(TG))
        else:
            sim = (b * 1.0)/min(len(GG),len(TG))

        cmd = "echo {0},{1},{2} >>{3}".format(apks[0],apks[1],sim,"similarityResult.txt")
        os.system(cmd)

        tips = "compare the {0},{1},sim:{2},b:{3},{4},{5}".format(apks[0],apks[1],sim,b,len(GG),len(TG))
        print tips 
        
        orif.close()
        tarf.close()


VF(oriGPath,repGpath)


print "all work is done!\n"






    

