#!/usr/bin/env python
# coding=utf-8
# author   : Chicho
# running  : python createGraph.py
# date     : 2017-07-16
# function : extract the signature and create the graph

import os

path = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/graph/filter/sig/"

graphPath = "/home/chicho/workspace/repackaged/DNADroid/experiment/falsepositive/graph/filter/graph/"



def createGraph():

    apkList = os.listdir(path)

    for apk in apkList:
        apkPath = os.path.join(path,apk)

        f = open(apkPath)

        lines = f.readlines()

        for line in lines:

            if ":" and ";" in line:
                line = line.replace("\n","")

                segs = line.split(";")

                if len(segs)==2:
                    continue

                graphName = segs[0]

                apkgraphPath = os.path.join(graphPath,apk)

                cmd = "echo '{0}' >> {1}".format(graphName,apkgraphPath)
                os.system(cmd)


                for i in range(2,len(segs)):

                    if "," not in segs[i] and ":" in segs[i]:
                        edges = segs[i].split(":")

                        cmd = "echo {0} {1} >> {2}".format(edges[0],edges[1],apkgraphPath)
                        os.system(cmd)

                    if ":" in segs[i] and "," in segs[i]:
                        items = segs[i].split(":")

                        edges = items[1].split(",")

                        for index in range(len(edges)):
                            cmd = "echo {0} {1} >> {2}".format(items[0],edges[index],apkgraphPath)
                            os.system(cmd)


        print apk 


        f.close()



createGraph()

print "all work is done!"
