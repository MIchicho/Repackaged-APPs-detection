#!/usr/bin/env python
# coding=utf-8
import os
import sys 


if (len(sys.argv)<2):

    # print tip info

    print'''
    =========================================================
    You can use the default GuiHierarchy files' path or input the path you like!
    usage : python extractStructFeature.py 
    you need to input <GuiHierarchy_path> or employ the default path
    e.g. sootAndroidOut
    Input : 0 -> default path
    Input : 1 -> your personal path
    =========================================================
    '''


    input = raw_input("you choice? 0 or 1:\n")

    while (input != '0') and (input != '1'):
        print "you input is wrong!"
        input = raw_input("you choice? 0 or 1:\n")


    if ( input == "0" ):
        print "you choose the default path! ...processing...\n" 
        path = "/home/chicho/Workspace/ResDroid/experiment/kdtree/KDOutput.txt"
    else:
        path = raw_input("you GUI file path:\n")
        if not os.path.exists(path):
            print "Cannot find the path, please check you input path!:p\n"
            sys.exit(1)


f = open(path,'r')

tmplist = []
alllist = []
dist = {}

i = 0

for line in f.readlines():
    line = line.replace("\n","")
    res = line.split(":")
    cno = res[0]
    element = res[1]
    
    if (element in alllist):
        continue


    if tmplist == []:
        tmplist.append(cno)
        tmplist.append(element)

        alllist.append(cno)
        alllist.append(element)

        per = cno 

    elif (tmplist != [] and cno == per):
        tmplist.append(element)
        alllist.append(element)

    elif (tmplist != [] and cno != per):
        dist[i]=tmplist
        i+=1
        tmplist=[]
        tmplist.append(cno)
        tmplist.append(element)

        alllist.append(cno)
        alllist.append(element)

        per = cno


print "the total cluster:",len(dist)


for k in dist:
    print len(dist[k]),dist[k]

    if k ==10:
        break


    

        


        








f.close()


