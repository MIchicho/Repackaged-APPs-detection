#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho
# Running  :  python getEventHandler.py 
# Date     :  2017-10-16 
# Function :  1. parse the Gator result and get the event handler

import os 
import time 
import xml.dom.minidom 
import sys
import numpy 
import Levenshtein




oriPath = "/home/chicho/result/sootAndroidOut/original/"

repPath = "/home/chicho/result/sootAndroidOut/repackaged/"

pairPath = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"

eventDistPath = "/home/chicho/workspace/repackaged/ResDroid/event/Eventedit_distance.csv"


def edit_distance(s1,s2):

    distance = Levenshtein.distance(s1,s2)

    ratio = Levenshtein.ratio(s1,s2)


    print "********************************"
    
    print "**********edit_distance*********"

    return (distance,ratio)




def getEventHandler(path):

    try:
        dom = xml.dom.minidom.parse(path)
    except:
        return 

    root = dom.documentElement

    eventList = root.getElementsByTagName('EventAndHandler')

    eventSeqList = []

    for eventHandler in eventList:
        event = eventHandler.getAttribute('event').replace(" ","")

        if eventHandler.hasAttribute('realHandler'):
            handler = eventHandler.getAttribute('realHandler').split(":")[1].replace(" ","")
        elif eventHandler.hasAttribute('handler'):
            handler = eventHandler.getAttribute('handler').split(":")[1].replace(" ","")

        eventHandlerName = event + handler

        eventSeqList.append(eventHandlerName)

    eventSeqList.sort()

    print eventSeqList

    eventSeq = ''.join(eventSeqList)


    return eventSeq


#*********************************************************

def find_lcseque(s1,s2):
    
	 # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果

        try:
	    m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ] 
        except:
            return 0 



	# d用来记录转移方向
	d = [ [ None for x in range(len(s2)+1) ] for y in range(len(s1)+1) ] 

	for p1 in range(len(s1)): 
		for p2 in range(len(s2)): 
			if s1[p1] == s2[p2]:            #字符匹配成功，则该位置的值为左上方的值加1
				m[p1+1][p2+1] = m[p1][p2]+1
				d[p1+1][p2+1] = 'ok'          
			elif m[p1+1][p2] > m[p1][p2+1]:  #左值大于上值，则该位置的值为左值，并标记回溯时的方向
				m[p1+1][p2+1] = m[p1+1][p2] 
				d[p1+1][p2+1] = 'left'          
			else:                           #上值大于左值，则该位置的值为上值，并标记方向up
				m[p1+1][p2+1] = m[p1][p2+1]   
				d[p1+1][p2+1] = 'up'         
	(p1, p2) = (len(s1), len(s2)) 
#	print numpy.array(d)
	s = [] 
	while m[p1][p2]:    #不为None时
		c = d[p1][p2]
		if c == 'ok':   #匹配成功，插入该字符，并向左上角找下一个
			s.append(s1[p1-1])
			p1-=1
			p2-=1 
		if c =='left':  #根据标记，向左找下一个
			p2 -= 1
		if c == 'up':   #根据标记，向上找下一个
			p1 -= 1
	s.reverse()

        LCS = ''.join(s)

	return len(LCS)



#*************************************************

def parseEventHandler(pairPath):

    start = time.time()

    f = open(pairPath)
    
    lineList = f.readlines()

    ef = open(eventDistPath)

    eflineList = ef.readlines()
    
    eventLineList = []

    for line in eflineList:
        line = line.replace("\n","")
        segs = line.split(",")

        newline = segs[0] + "," + segs[1]

        eventLineList.append(newline)

    for line in lineList:
        line = line.replace("\n","")

        if line in eventLineList:
            print "existing ... ... "
            continue 

        

        segs =line.split(",")
    
        oriapk = segs[0]
        repapk = segs[1]

        oriapkPath = os.path.join(oriPath,oriapk+".xml")
        repapkPath = os.path.join(repPath,repapk+".xml")

        if os.path.exists(oriapkPath) and os.path.exists(repapkPath):
            print oriapk 
            oriSeq = str(getEventHandler(oriapkPath))
            
            print repapk 
            repSeq = str(getEventHandler(repapkPath))

            if len(oriSeq) > 20000 or len(repSeq)>20000:
                continue


            if len(oriSeq)==0 or len(repSeq)==0:
                continue 

            lenthLCS = find_lcseque(oriSeq,repSeq)
            
            try:
                distance = 1 - lenthLCS*1.0/min(len(oriSeq),len(repSeq))
            except:
                continue 


            print oriapk,repapk,str(distance)

            cmd = "echo {0},{1},{2}>>{3}".format(oriapk,repapk,distance,"eventhandler_LCSdistance.csv")
            os.system(cmd)


            # edit_distance 

            edit_dist,ratio = edit_distance(oriSeq,repSeq)

            print oriapk,repapk,str(edit_dist),str(ratio)

            cmd = "echo {0},{1},{2},{3}>>{4}".format(oriapk,repapk,edit_dist,ratio,"Eventedit_distance.csv")
            os.system(cmd)
            

            print "\n\n"


    end = time.time()
    
    elapse = end - start

    cmd = "echo {0}>>{1}".format(elapse,"event_time")
    os.system(cmd)



parseEventHandler(pairPath)


print "all work is done!"
        
            
