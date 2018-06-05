#!/usr/bin/env python
# coding=utf-8

import os
from numpy import array
import numpy as np
import random
import math
import matplotlib.pyplot as pl

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/ori_nodelete_CFG.csv"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/rep_nodelete_CFG.csv"

orif=open(oriPath)
repf=open(repPath)

def get_data(lines):

    sizeArry=[]

    for line in lines:
        line = line.replace("\n","")

        line = int(line)

        sizeArry.append(line)

    return array(sizeArry)

oriLenths = get_data(orif.readlines())

repLenths = get_data(repf.readlines())


def draw_hist(lenths,name):
    data = lenths 

    
    bins = np.linspace(min(data),max(data),30)

    

    pl.hist(data,bins)

    pl.semilogx()
    

    pl.xlabel('Number of CFG per application')

    pl.ylabel('Number of occurences')

    titleStr = 'Frequency distribution of number of CFGs of {0} apps'.format(name)

    pl.title(titleStr)

    pl.show()

    picName = name + "_bins20Ads.png"
    pl.savefig(picName)

draw_hist(oriLenths,"original")
#draw_hist(repLenths,"repackaged")
