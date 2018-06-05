#!/usr/bin/env python
# coding=utf-8

import os
import math 
from numpy import array 
import numpy as np 
import pylab as pl 

graphPath = "/home/chicho/workspace/repackaged/MassVet/graphDict.csv"

f = open(graphPath)

def get_data(lines):

    sizeArry = []

    for line in lines:
        line = line.replace("\n","")

        segs = line.split(",")

        try:
            apkCnt = int(segs[1])
        except:
            print segs[0]

        sizeArry.append(apkCnt)

    return array(sizeArry)

lenths = get_data(f.readlines())

def draw_hist(lenths):
    data = lenths

    bins = np.linspace(min(data),max(data),20)

    pl.hist(data,bins)

    pl.ylabel('Number of Apps')

    pl.title('Distribution of the ATG number')

    pl.show()

draw_hist(lenths)

