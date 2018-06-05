#!/usr/bin/env python
# coding=utf-8

import os
from numpy import array
import numpy as np
import random
import math
import pylab as pl

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


def draw_hist(lenths1,lenths2):
    data1 = lenths1
    data2 = lenths2 

    fig,axes = pl.subplots(nrows=2, ncols=1)

    ax0, ax1 = axes.flatten()

    bins0 = np.linspace(min(data1),4000,40)

    ax0.hist(data1,bins0)

    pl.xlabel('Number of CFG per application')

    pl.ylabel('Number of occurences')

    ax0.set_title('Frequency distribution of number of CFG of original apps')

    bins1 = np.linspace(min(data2),4000,40)

    ax1.hist(data2,bins1)

    ax1.set_title('Frequency distribution of number od CFG of repackaged apps')

#    fig.tight_layout()

    pl.show()



#draw_hist(oriLenths)
draw_hist(oriLenths,repLenths)
