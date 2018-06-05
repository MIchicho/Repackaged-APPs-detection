#!/usr/bin/env python
# coding=utf-8

import os 
import networkx as nx 
import matplotlib.pyplot as plt 

oriGpath = "/home/chicho/workspace/repackaged/ViewDroid/moreGraph/original/2FA09CF23FE00751F2A0581022C5B4887F5C313E76BBFB70F339D2E34B326FE7"

repGPath = "/home/chicho/workspace/repackaged/ViewDroid/updateResult/repackaged/93756E7F3E51818D4EC91F5FC4F3A32C6EFA8FA0A4E62C5F35EA6735E51D77BD"

def drawGraph(path):

    orif=open(repGPath)

    lines = orif.readlines()

    i = 0 
    GL = []

    while(i<len(lines)):

        line = lines[i]

        if " " not in line:
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

        if Gname not in GL:
            GL.append(Gname)
    
    j = 0
    for G in GL:
        nx.draw(G)
#        plt.show()
        gname = path.split("/")[-1] + "graph_" + str(j) + ".png"
        plt.savefig(gname)
        j = j + 1

drawGraph(repGPath)

