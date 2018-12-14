#!/usr/bin/env python
# coding=utf-8
import os
import math 
import numpy as np
from numpy import array
import matplotlib.pyplot as pl 

path = "/home/chicho/workspace/repackaged/ResDroid/similarScore/similarScore.csv"

f = open(path) 

def get_data(lines):

    sizeArry = []

    for line in lines:
        line = line.replace("\n","")

        segs = line.split(",")

        sim = float(segs[2])

        sizeArry.append(sim)

    return array(sizeArry)


lenths = get_data(f.readlines()) 

def draw_hist(lenths):
    data = lenths 

    bins = np.linspace(min(data),max(data),20)

#    pl.hist(data,bins,histtype='stepfilled',facecolor='palegreen')


    pl.hist(data,bins,facecolor='darkviolet')

 #   pl.xscale('log')
#    pl.ylabel('log')

    pl.xlabel('Euclidean Distance')

    pl.ylabel('Number of Application Pairs')

    pl.show()

draw_hist(lenths)



