#!/usr/bin/env python
# coding=utf-8
import os
import numpy as np
import sys
import statsmodels as sm
from numpy import array 
import matplotlib.pyplot as plt 
from scipy.stats import cumfreq



path = "/home/chicho/workspace/repackaged/ResDroid/event/weight"



#*****************************************
def get_data(lines):

    sizeArray = []
    for line in lines:
        line = line.replace("\n","")
        segs = line.split(",")

        try:
            actCnt = float(segs[2])
        except:
            print segs[0]

        sizeArray.append(actCnt)


    return array(sizeArray)



#************************************
def readFile(path):

    fileList = os.listdir(path)

    colors = ['r','g','b','y','c','m','k','coral','lawngreen']
    
    i = 0
    for file in fileList:
        filePath = os.path.join(path,file)

        f = open(filePath)

        lenths = get_data(f.readlines())

        f.close()

        

        cdf_plot(lenths,colors[i])

        i = i + 1






#**********************************************
def cdf_plot(lenths,color):
    data =lenths 
    
    counts,bin_edges = np.histogram(data, 15000, normed=True)
    cdf = np.cumsum(counts)
    

    #plt.plot(bin_edges[1:],cdf,lw=2)
    # if we want to set the color 
    plt.plot(bin_edges[1:],cdf,lw=2,color=color)

    plt.xlabel('Number of Activity')
    plt.ylabel('CDF')

    plt.grid(True)

    plt.show()




readFile(path)

