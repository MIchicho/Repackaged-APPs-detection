#!/usr/bin/env python
# coding=utf-8

import os 
import math
from numpy import array
import numpy as np
import pylab as pl

nodePath = "/home/chicho/workspace/repackaged/DNADroid/node/nodeavg.csv"

f = open(nodePath)

def get_data(lines):

    sizeArry= []

    for line in lines:
        line = line.replace("\n","")

        line = int(line)

        sizeArry.append(line)

    return array(sizeArry)

lenths = get_data(f.readlines())


def draw_hist(lenths):
    data = lenths

    bins = np.linspace(min(data),20,10)

    pl.hist(data,bins)

    pl.ylabel('Number of Applications')

    pl.title('Distribution of the node average number in PDG')

    pl.show()


draw_hist(lenths)

