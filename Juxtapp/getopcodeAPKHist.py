#!/usr/bin/env python
# coding=utf-8

import os 
from numpy import array
import numpy as np
import random
import math
import pylab as pl

oriPath = "/home/chicho/workspace/repackaged/Juxtapp/code/oriInstrNum.csv"

repPath = "/home/chicho/workspace/repackaged/Juxtapp/code/repInstrNum.csv"

orif = open(oriPath)
repf = open(repPath)



def get_data(lines):

    sizeArry=[]

    for line in lines:
        line = line.replace("\n","")

        line = int(line)

        sizeArry.append(line)

    return array(sizeArry)


oriLenths = get_data(orif.readlines())

repfLenths = get_data(repf.readlines())


def draw_hist(lenths):
    data = lenths

    bins = np.linspace(min(data),max(data),200)


   # bins = np.linspace(50,50000,150)

    pl.xlim([min(data)-5,max(data)+5])

   # pl.hist(data,bins,color='lawngreen',histtype='stepfilled')
    
    pl.hist(data,bins)

    pl.xlabel('Number of opcodes per application')

    pl.ylabel('Number of occurences')
    
    pl.title('Frequency distribution of number of opcodes of apps')

    pl.show()



draw_hist(oriLenths)

draw_hist(repfLenths)

