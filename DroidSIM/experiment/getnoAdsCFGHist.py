#!/usr/bin/env python
# coding=utf-8
#  Author   : Chicho
#  Date     : 2017-05-16
#  function : draw the hist of CFG (delete the Ads)

import os 
from numpy import array
import numpy as np
import random 
import math 
import pylab as pl 

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/ori_nodelete_CFG.csv"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/rep_nodelete_CFG.csv"

orif = open(oriPath)
repf = open(repPath)

def get_data(lines):

    sizeArry=[]

    for line in lines:
        line = line.replace("\n","")

        line = int(line)

        sizeArry.append(line)

    return array(sizeArry)

lines = orif.readlines() + repf.readlines()

lenths = get_data(lines)

#oriLenths = get_data(orif.readlines())
#repLenths = get_data(repf.readlines())



def draw_hist(lenths):
    data = lenths

    bins = np.linspace(min(data),max(data),100)

    pl.hist(data,bins)

    pl.xlabel('Number of Methods of Per APP')

    pl.ylabel('Number of occurences')

    pl.title('Frequency distribution of the number of methods of apps with ad libraries')

    pl.show()


#draw_hist(oriLenths)
draw_hist(lenths)
