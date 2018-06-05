#!/usr/bin/env python
# coding=utf-8
#  Author  :  Chicho
#  Date    :  2017-10-20 
#  Function : 1. calculate the similar and get the best weight 

import os
import time 
import sys

ACTdist = "/home/chicho/workspace/repackaged/ResDroid/experiment/fpfn/ACTdistance.csv"


eventDist = "/home/chicho/workspace/repackaged/ResDroid/experiment/fpfn/eventhandler_LCSdistance.csv"

parameter = "/home/chicho/workspace/repackaged/ResDroid/experiment/fpfn/parameter8"


def calSimilar(wa,we,filename):

    af = open(ACTdist)

    aflineList = af.readlines()

    ef = open(eventDist)

    eflineList = ef.readlines()
    
    
    for line in aflineList:
        line = line.replace("\n","")
        print "line in activity"
        print line 
        segs = line.split(",")

        newline = segs[0] + "," + segs[1]

        print "newline"
        print newline

        for eline in eflineList:
            eline = eline.replace("\n","")

            print "eline:"
            print eline

             
            
            if newline in eline:
                print "Yes,we find your bro!"
                print eline 

                print "print weight of activity and weight of event handler!"
                print wa,we 

                oriapk = line.split(",")[0]
                repapk = line.split(",")[1]
                actSimilar = float(line.split(",")[2])

                eventSimilar = float(eline.split(",")[2])

                distance = actSimilar * wa + eventSimilar * we

                print "distance:"
                print distance 

                cmd = "echo {0},{1},{2}>>{3}".format(oriapk,repapk,distance,filename)
                os.system(cmd)

        




#*****************************************************
#   parse the parmeter
#*****************************************************

def getParameter():
    f =open(parameter)

    linelist = f.readlines()

    for line in linelist:
        line = line.replace("\n","")
        segs = line.split(",")

        wa = float(segs[0])
        we = float(segs[1])
        filename = segs[2]

        calSimilar(wa,we,filename)




getParameter()


print "all work is done!"


