#!/usr/bin/env python
# coding=utf-8
# author   :  Chicho
# running  :  python featureHashing.py
# function :  Calculate the Feature Hashing

import os
from random import shuffle


input = raw_input("you choice ? 0 or 1 :\n")

while (input != '0') and (input != '1'):
    print "you input is wrong!"
    input = raw_input("you choice ? 0 or 1:\n")

if (input == '0'):
    print "you choose the original path! ...processing...\n"
    Path = "/home/chicho/workspace/repackaged/Juxtapp/original/"
elif ( input =='1' ):
    print "you choose the repackaged path! ...processing...\n"
    Path = "/home/chicho/workspace/repackaged/Juxtapp/repackaged/"


poolPath = "/home/chicho/workspace/repackaged/Juxtapp/pool"

poolList = os.listdir(poolPath)

# generate the n-grams

def generateKgram(fileLine,K):

    kgram = []

    for i in range(len(fileLine)):
        if (i+K > len(fileLine)):
            break

        shingle = fileLine[i:i+K]

        kgram.append(shingle)


    return kgram 


def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)

    return hash 


def hashing_vectorizer(kgram,N):
    x = [0 for i in xrange(N)]
    
    for shingle in kgram:
        h = hash_djb2(shingle)
    
        x[h%N] += 1
        
    return x


def readFile():

    fileList = os.listdir(Path)

    shuffle(fileList)

    for file in fileList:
        
        if file in poolList:
            print file + " exists...."
            continue

        filePath = os.path.join(Path,file)

        tip="Now we are processing the {0}.apk".format(file)
        print tip



        f=open(filePath)
        
        # to get all the line 
        linelist = []

        for line in f.readlines():
            line = line.replace("\n","")
            linelist.append(line)

        fileLine = "".join(linelist)

        print fileLine

        eachFileKgram=generateKgram(fileLine,100)
        
        bitvector = hashing_vectorizer(eachFileKgram,10007)

        bitVecStr = map(str,bitvector)

        filename=file.split(".")[0]

        bitString = ",".join(bitVecStr)
        
        print "\n\n\n"

        print bitString

        print "\n\n\n"
        cmd="echo {0},{1} >> {2}".format(filename,bitString,"reData.csv")
        os.system(cmd)

        cmd = filename + "," + bitString + "\n"
        
       # fo.write(cmd)
        
        # let more processing handle the project
        poolFilePath = os.path.join(poolPath,file)
        cmd = "touch {0}".format(poolFilePath)
        os.system(cmd)

        
    
'''
fo=open("data.csv","a+")
readFile()
fo.close()
'''

readFile()

print "all work is done!\n"
