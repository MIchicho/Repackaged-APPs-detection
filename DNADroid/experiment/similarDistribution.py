#!/usr/bin/env python
# coding=utf-8

import os
import math
from numpy import array
import numpy as np
import pylab as pl

simPath = "/home/chicho/workspace/repackaged/DNADroid/filter/similarScore.csv"

f = open(simPath)

def get_data(lines):
    
    minArry = []
    maxArry = []

    for line in lines:
        line = line.replace("\n","")

        segs = line.split(",")

        sim1 = float(segs[2])

        sim2 = float(segs[3])

        minValue = min(sim1,sim2)

        minArry.append(minValue)

        maxValue = max(sim1,sim2)

        maxArry.append(maxValue)


    minList = array(minArry)
    maxList = array(maxArry)

    return (minList,maxList)


lenths1,lenths2 = get_data(f.readlines())

def draw_hist2(lenths):
    data = lenths 

 #   bins = np.linspace(min(data),max(data),10)
    bins = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

    rects = pl.hist(data,bins,color="greenyellow")

    pl.xlabel('Similarity Value Range(%)')

    pl.ylabel('# of app pairs whose smaller Similarity score is in range')

    
    for x,y in zip(rects[1],rects[0]):
        x_pos = float(x) 
        height = int(y)+2
        pl.text(x_pos,height, "%d" % int(y))

    

    pl.show()

draw_hist2(lenths2)
