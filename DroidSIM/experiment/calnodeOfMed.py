#!/usr/bin/env python
# coding=utf-8
# Function :  1.calculate the avg node of all method
#             2. calculate the maximum node 

import os 

oripath = "/home/chicho/workspace/repackaged/DroidSIM/delete/original1/"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/delete/repackaged1/"


oriList = os.listdir(oripath)

repList = os.listdir(repPath) 


def calculateNode(Path,fileList):

    max = 0
    
    Less4 =0

    sum = 0.0

    for file in fileList:
        filePath = os.path.join(Path,file)

        f = open(filePath)

        lines = f.readlines()

        for line in lines:
            line = line.replace("\n","")

            segs = line.split(";")

            nodeNum = int(segs[1])

            sum += nodeNum

            if nodeNum<=4:
                Less4 +=1

            if max < nodeNum:
                max = nodeNum
            
            if nodeNum ==0:
                continue 
            
            cmd = "echo {0}>>{1}".format(nodeNum,"Node.csv")
            os.system(cmd)

      
      

        avg = sum*1.0/len(lines)

        cmd = "echo {0}>>{1}".format(avg,"AvgNode.csv")
        os.system(cmd)

        sum = 0

               
    

calculateNode(oripath,oriList)
calculateNode(repPath,repList)



