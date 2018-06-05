#!/usr/bin/env python
# coding=utf-8
#  Author   :  Chicho
#  Date     :  2017-06-07
#  Function :  Parse the CFG signature(handled by the CFGScanDroid)
#              the output result will ouput the path 
#              /home/chicho/workspace/repackaged/DroidSIM/graph/ 

#****************************************
# Using method :
# java -jar CFGScanDroid.jar
#
# before we run this file we should run the CFGScanDroid
# sudo apt-get install maven
# ./build.sh 
#  This will create a file:
# target/CFGScanDroid.jar
#***********************************************

'''
Before we create the CFGScanDroid.jar we need to run the getSignature.py
python getSignature.py
we will create a signature for each APK and store the into the relative path 
'''




#**********************************************************************
#  when we use CFGScanDroid scan the dex file we can get the signature 
#  of each apk (CFG)
#  the signature format:
#  La.a()Z;8;0:1,2,3,4,5;6:7
#  interceptSMS;4;0:1,2;1:3;2:3,0
#  the signature name is interceptSMS, there are 4 vertices
#  0:1,2
#  1:3
#  2:3,0
#  in this way we can get the edge relation
#  
#  the edges:
#  0->1
#  0->2
#  1->3
#  2->3
#  2->0
#**********************************************************************

import os

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/graph/ori/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/graph/rep/"

orioutPath = "/home/chicho/workspace/repackaged/DroidSIM/graph/"

repoutPath = "/home/chicho/workspace/repackaged/DroidSIM/graph/"

def parseSig(path,outPath):
    
    fileList = os.listdir(path)

    for file in fileList:
        filePath = os.path.join(path,file)

        f = open(filePath,'r')

        fileoutPath = os.path.join(outPath,file)

        j = 0 
        
        for line in f.readlines():

            if ":" and ";" in line: # find the line La().a;4;0:1,2;1:3;2:3,0 
                graphNo = "t" + str(j)             

                line = line.replace("\n","")

                segs = line.split(";")   # 0:1,2  1:3   2:3,0
                
                if len(segs) == 2:  # handled this situation
                    continue        # La().a;2 

                
                cmd = "echo {0} >> {1}".format(graphNo,fileoutPath)  # output t1
                os.system(cmd)                                          
                
                for i in range(2,len(segs)):

                    if "," not in segs[i] and ":" in segs[i]:  # 1:3 1->3
                        edges = segs[i].split(":")

                        cmd = "echo {0} {1} >> {2}".format(edges[0],edges[1],fileoutPath)
                        os.system(cmd)

                    if ":" in segs[i] and "," in segs[i]:    # 0:1,2
                        items = segs[i].split(":")           # items[0]:0 items[1]: 1,2

                        edges = items[1].split(",")          # split the itmes[1]
                                                             # 1 2 edges = [1,2]

                        for index in range(len(edges)):
                            cmd = "echo {0} {1} >> {2}".format(items[0],edges[index],fileoutPath)
                            os.system(cmd)                   # output 0->1 0->2

            j = j + 1 

        print "we are handled the {0}...".format(file)



parseSig(oriPath,orioutPath)

print "original file finished!"

parseSig(repPath,repoutPath)

print "all work is done!"


