#!/usr/bin/env python
# coding=utf-8


import os 
import networkx as nx
from networkx.algorithms import isomorphism 
import time 

i = 0

#oriGPath = "/home/chicho/workspace/repackaged/DroidSIM/code/"

#tarGPath = "/home/chicho/workspace/repackaged/DroidSIM/code/CFG1.txt"

oriGPath = "/home/chicho/test/test/033E564620E5E45F79E707D230BB7BE2AB600F1F524A3D337FE1785EF393DEEC.txt"

tarGPath = "/home/chicho/test/test/513DFE51A807B28866411DA60619E3D992CF77AEA79218E165CD78A4B9F23829.txt"

GG=[]
TG=[]

def VF(lines):
    GL = []

    '''
    for i in range(len(lines)):
        
        line = lines[i]

        if " " not in line:
            Gname = line.replace("\n","")
            
            Gname = nx.Graph()

            for j in range(i+1,len(lines)):
                edge = line.split(" ")
                Gname.add_edge(edge[0],edge[1])


        if Gname not in GG:
            GG.apend(Gname)


    '''

    i = 0

    while(i < len(lines)):

        line = lines[i]

        if " " not in line:
            Gname = line.replace("\n","")

            Gname = nx.Graph()

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


orif = open(oriGPath)
tarf = open(tarGPath)

GG=VF(orif.readlines())
TG=VF(tarf.readlines())

#print GG[1].edges()
#print TG[1].edges()

'''
print len(GG[1].edges())
print len(TG[1].edges())
GM = isomorphism.GraphMatcher(GG[1],TG[1])

print GM.subgraph_is_isomorphic()

print GM.mapping
'''


def VF2(GG,TG):
    '''
    this function is used to find the subgraph isomorphism 
    '''
    
    b = 0
    start = time.time()

    for G in GG:

        for T in TG:

            GM = isomorphism.GraphMatcher(G,T)
            GM1 = isomorphism.GraphMatcher(T,G)

            if GM.subgraph_is_isomorphic():
                print "GM there are isomorphism:"
                print GM.mapping
                       
                print "++++++++++++++++++++++++" 
                print G.edges()
                print T.edges()
                
                b = b + 1
                break
            else:
                print "GM is not isomorphic!"

            if GM1.subgraph_is_isomorphic():
                print "GM1 is isomorphism:"
                print GM1.mapping 
                
                #b = b + 1
                print "************************"
                print G.edges()
                print T.edges()
                break 
            else:
                print "GM1 is not isomorphic!"
        
            print "every iterate~"
            print str(time.time() - start)

            if int(time.time()-start) > 5:
                print "*******"
                print "***********"
                print "times up"
                break 

        print "every circile"
        elapse = time.time() - start
        print elapse
        

    print "==============================="
    print "*******************************"
    print time.time() - start 
    
    return b 

print "GG number:" + str(len(GG))
print "TG number:" + str(len(TG))

#sim = b*1.0/min(len(GG),len(TG))

if len(GG)<len(TG):
    b=VF2(GG,TG)
if len(GG)>len(TG):
    b=VF2(TG,GG)

print "b:" + str(b)

print "GG number:" + str(len(GG))

print "TG number:" + str(len(TG))

sim = b*1.0/max(len(GG),len(TG))
print "sim:" + str(sim) 
