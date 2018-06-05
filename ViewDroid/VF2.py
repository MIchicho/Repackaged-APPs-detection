#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho
# filename :  VF.py
# Version  :  2.0
# Date     :  2017-06-30 
# function :  1.parse the graph files of ATG
# the newset version

import os 
import networkx as nx
from networkx.algorithms  import isomorphism
import time 

oriGpath = "/home/chicho/workspace/repackaged/ViewDroid/updateResult/original/"

repGpath = "/home/chicho/workspace/repackaged/ViewDroid/updateResult/repackaged/"

pairPath = "/home/chicho/workspace/repackaged/repackaging_pairs1.txt"


def createGraph(lines):
    GL = []

    i = 0

    while(i < len(lines)):

        line = lines[i]

        if " " not in line: #we find the graph name
            Gname = line.replace("\n","")

            Gname = nx.DiGraph()

            i = i + 1

            line = lines[i]

            while ((" " in line) and (i<len(lines))):
                line = line.replace("\n","")
                edge = line.split(" ")
                Gname.add_edge(int(edge[0]),int(edge[1]))

                i = i + 1

                if i < len(lines):
                    line = lines[i]



        if Gname  not in GL:
            GL.append(Gname)



    if len(GL) == 1:
        return GL


    if len(GL) >1:
        edgelist =[]
        for G in GL:
            Gedges = len(G.edges())
            edgelist.append(Gedges)

        if len(set(edgelist))==1 and edgelist[0]==2:
            return GL
        else:
            newGL=[]

            for G in GL:

                edgeCnt = len(G.edges())
                if edgeCnt > 1:
                    newGL.append(G)

            return newGL

        


        '''

        edgeCnt = len(Gname.edges())
        if edgeCnt <=1:
            continue

        else:
            if Gname not in GL:
                GL.append(Gname)
        '''



    return GL 




def VF2(oriGpath,repGpath):

    f = open(pairPath)

    

    for line in f.readlines():
        

    

        line = line.replace("\n","")
        apks = line.split(",")

        oriapk = apks[0]
        repapk = apks[1]

        tips = "compare the apk pairs {0},{1}".format(apks[0],apks[1])
        print tips
        
        print "*+++++++++++++++++**********+++++++++++++++++++++++++++++++"
        oriAPKPath = os.path.join(oriGpath,oriapk)
        repAPKPath = os.path.join(repGpath,repapk)


        if os.path.exists(oriAPKPath) and os.path.exists(repAPKPath):
            orif = open(oriAPKPath)
            repf = open(repAPKPath)

        else:
            if not os.path.exists(oriAPKPath) and os.path.exists(repAPKPath):
                cmd = "echo {0} >> {1}".format(oriapk,"orinoexists.txt")
                os.system(cmd)
                tips = "the original apk {0} not exists".format(oriapk)
                print tips 

            if not os.path.exists(repAPKPath) and os.path.exists(oriAPKPath):
                cmd = "echo {0} >> {1}".format(repapk,"repnoexists.txt")
                os.system(cmd)
                tips = "the repackaged apk {0} not exists".format(repapk)
                print tips 

            if not os.path.exists(repAPKPath) and os.path.exists(oriAPKPath):
                cmd = "echo {0},{1} >> {2}".format(oriapk,repapk,"noexists.txt")
                os.system(cmd)
                tips = "the apk {0},{1} not exists".format(oriapk,repapk)
                print tips 

            continue 
        

        GG = createGraph(orif.readlines())
        TG = createGraph(repf.readlines())

        

        avgsimilar = 0.0

        i = 0 

        
        num = 0

        GListCnt = len(GG)
        TListCnt = len(TG)

        
        
        print "The graph numbers of original: {0}".format(GListCnt)
        print "The graph numbers of repackaged: {0}".format(TListCnt)


        if GListCnt ==0:
            cmd = '''echo "parse get no node of "{0}>>{1}'''.format(oriapk,"orinoexists.txt")
            os.system(cmd)

        if TListCnt ==0:
            cmd = '''echo "parse get no nodes of " {0} >> {1}'''.format(repapk,"repnoexists.txt")
            os.system(cmd)

        if GListCnt ==0 or TListCnt ==0:
            continue 


        start = time.time()

        if GListCnt <= TListCnt:
            print "G<=T"
            for i in range(len(TG)):

                for G in GG:

                    for T in TG:

                        G_edgesCnt = len(G.edges())
                        T_edgesCnt = len(T.edges())

                        print "G_edges:"
                        print G.edges()

                        print "T_edges:"
                        print T.edges()

                        print "*******nodes***"
                        print G.nodes()

                        print "***********"
                        print T.nodes()

                        Gnodes = len(G.nodes())
                        Tnodes = len(T.nodes())


                        if G_edgesCnt >= T_edgesCnt:
                            GM = isomorphism.DiGraphMatcher(G,T)
                        else:
                            GM = isomorphism.DiGraphMatcher(T,G)

                
                        if GM.subgraph_is_isomorphic():
                            print GM.mapping
                            mCnt = len(GM.mapping)
                            print "the number of matching nodes is {0}".format(mCnt)
                            print "Gnodes: {0}".format(Gnodes)
                            print "Tnodes: {0}".format(Tnodes)

                            avg = mCnt*1.0/min(Gnodes,Tnodes)
                            
                            avgsimilar += avg 
                            num += 1

                            GG.remove(G)
                            TG.remove(T)
                            
                            
                            print "average number: " + str(avg)
                            print avgsimilar
                            
                            break
                    
                    break 

                if len(GG)==0 or len(TG)==0:
                    break 

        else:

            for k in range(len(GG)):

                for G in GG:

                    for T in TG:

                        G_edgesCnt = len(G.edges())
                        T_edgesCnt = len(T.edges())

                        Gnodes = len(G.nodes())
                        Tnodes = len(T.nodes())

                    
                    if G_edgesCnt >= T_edgesCnt:
                        GM = isomorphism.DiGraphMatcher(G,T)
                    else:
                        GM = isomorphism.DiGraphMatcher(T,G)


                    if GM.subgraph_is_isomorphic():
                        print GM.mapping
                        mCnt = len(GM.mapping)

                        print "the number of matching nodes is {0}".format(mCnt)
                        print "Gnodes : {0}".format(Gnodes)
                        print "Tnodes : {0}".format(Tnodes)

                        avg = mCnt*1.0/min(Gnodes,Tnodes)

                        avgsimilar += avg 
                        num += 1

                        GG.remove(G)
                        TG.remove(T)
                        print "avg : " + str(avg)
                        print "avgsimilar: " + str(avgsimilar)
                        break
                    break
                
                if ((len(GG)==0) or (len(TG)==0)):
                    break 

        if num!=0:
            avgsimilar = avgsimilar/num 
        
        print "the final avgsimilar: {0}".format(avgsimilar)
        end = time.time()

        time_interval = str(end-start)

        cmd = "echo {0},{1},{2}>>{3}".format(oriapk,repapk,time_interval,"runningtime.txt")
        os.system(cmd)

        cmd = "echo {0},{1},{2}>>{3}".format(oriapk,repapk,avgsimilar,"similarScore.txt")
        os.system(cmd)
        
        if avgsimilar != 0:
            cmd = "echo {0},{1},{2}>>{3}".format(oriapk,repapk,avgsimilar,"findsimilarResult.txt")
            os.system(cmd)

        tips = "compare the {0},{1},sim:{2},{3},{4}".format(oriapk,repapk,avgsimilar,Gnodes,Tnodes)
        print tips

        orif.close()
        repf.close()


VF2(oriGpath,repGpath)


print "all work is done!\n"
