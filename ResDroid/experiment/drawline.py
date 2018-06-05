#!/usr/bin/env python
# coding=utf-8
import numpy as np 
import pylab as pl 
import os
from numpy import array




path  = "/home/chicho/workspace/repackaged/ResDroid/event/weight/"

def get_data(lines):

    sizeArray = []
    yArray = []
    y = 0

    for line in lines:
        line = line.replace("\n","")
        segs = line.split(",")
        
        distance = float(segs[2])
            
        sizeArray.append(distance)

        yArray.append(y)

        y = y + 1


    return array(sizeArray),array(yArray)






def draw_line(lenths,xarray,labels):

    x = xarray 
    y = lenths

    
    

    pl.plot(x,y,label = 'line')


def readFile():

    fileList = os.listdir(path)

    colors = ['r','g','b','y','c','m','k','coral','lawngreen']
    
    i = 0
    for file in fileList:

        filePath = os.path.join(path,file)

        f = open(filePath)

        lenths,x = get_data(f.readlines())

        f.close()
        
        i = i + 1

        wl = i + 0.1 
        we = 1 - wl
        labels = 'weight: wl {0}, we {1}'.format(wl,we)
        draw_line(lenths,x,labels)

    pl.xlim(0,1800)
    pl.show()

    pl.legend()

readFile()

        


