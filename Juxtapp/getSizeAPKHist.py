#!/usr/bin/env python
# coding=utf-8

import os 
from numpy import array
import numpy as np
import random
import math
import pylab as pl

oriPath = "/home/chicho/workspace/repackaged/Juxtapp/code/originalSize.csv"

repPath = "/home/chicho/workspace/repackaged/Juxtapp/code/repackagedSize.csv"

orif = open(oriPath)
repf = open(repPath)



def get_data(lines):

    sizeArry=[]

    for line in lines:
        line = line.replace("\n","")

        size = int(line)/1000

        sizeArry.append(size)



    return array(sizeArry)

oriLenths = get_data(orif.readlines())

repfLenths = get_data(repf.readlines())


def draw_hist(lenths):
    data = lenths

    bins = np.linspace(min(data),max(data),150)


   # bins = np.linspace(50,50000,150)

    pl.xlim([min(data)-5,max(data)+5])

   # pl.hist(data,bins,color='lawngreen',histtype='stepfilled')
    pl.hist(data,bins)
    pl.xlabel('Size of the app(kb)')
    pl.ylabel('Number of occurences')
    
    pl.title('Frequency distribution of size of original APK files')

    pl.show()



draw_hist(oriLenths)

draw_hist(repfLenths)

