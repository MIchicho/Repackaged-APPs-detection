#!/usr/bin/env python
# coding=utf-8
#  Author   : Chicho
#  Date     : 2017-05-20 
#  Function : Parse the CFG signature(handled by the CFGScanDroid)

import os 

#Path = "/home/chicho/workspace/repackaged/tools/CFGScanDroid-master/target/signature.adb"

Path = "/home/chicho/test/test/test.adb"

f = open(Path,'r')

j = 0
for line in f.readlines():

    if ":" and ";" in line:
        graphNo = "t" + str(j)


        cmd = "echo {0} >> {1}".format(graphNo,"CFG.txt")
        os.system(cmd)

        line = line.replace("\n","")

        segs = line.split(";")

        print segs

        for i in range(2,len(segs)):

            print segs[i]

            if "," not in segs[i] and ":" in segs[i]:
                edges = segs[i].split(":")

                cmd = "echo {0} {1} >> {2}".format(edges[0],edges[1],"CFG.txt")
                os.system(cmd)

            if ":" in segs[i] and "," in segs[i]:
                items = segs[i].split(":")

                edges = items[1].split(",")

                for index in range(len(edges)):

                    cmd = "echo {0} {1} >> {2}".format(items[0],edges[index],"CFG.txt")
                    os.system(cmd)


        j = j + 1



print "all work is done!"


