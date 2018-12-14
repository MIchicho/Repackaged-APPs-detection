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

oriPath = "/home/chicho/workspace/repackaged/DroidSIM/original_delete_CFG.csv"

repPath = "/home/chicho/workspace/repackaged/DroidSIM/repackaged_delete_CFG.csv"

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
repLenths = get_data(repf.readlines())

def draw_hist(lenths):
    data = lenths

    bins = np.linspace(min(data),2000,20)

    pl.hist(data,bins)

    pl.xlabel('Number of CFG per application')

    pl.ylabel('Number of occurences')

    pl.title('Frequency distribution of number of CFG of repackaged apps without ad libraries')

    pl.show()


#draw_hist(oriLenths)
draw_hist(repLenths)
