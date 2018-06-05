#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho 
# Date     :  2017-10-10
# Running  :  python LCS.py 
# function :  1. use the deep first search algorithm to traverse the graph 
#             2. the graph comes from /home/chicho/workspace/repackaged/MassVet/graph/original/ 
#                and /home/chicho/workspace/repackaged/MassVet/graph/repackaged/ 


import numpy 
import os 
import time 
import networkx as nx
import Levenshtein 


oriPath = "/home/chicho/workspace/repackaged/MassVet/graph/original/"

repPath = "/home/chicho/workspace/repackaged/MassVet/graph/repackaged/"

pairPath = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"


def creategraph(lines):
    GL = []

    i = 0

    while(i<len(lines)):
        line = lines[i]

        
        if " " not in line:
            Gname = nx.DiGraph()

            i = i + 1

            line = lines[i]

            while ((" " in line) and (i < len(lines))):
                line = line.replace("\n","")
                edge = line.split(" ")
                Gname.add_edge(edge[0],edge[1])

                i = i + 1

                if i <len(lines):
                    line = lines[i]


        if Gname not in GL:
            GL.append(Gname)


    return GL 



#***************************************************
#***************************************************
def find_lcseque(s1, s2): 
	 # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
	m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ] 
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
	print numpy.array(d)
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



def dfs(GL):
    
    nodeSequence = ""

    for G in GL:
        dfsNodeList = list(nx.dfs_preorder_nodes(G))

        nodeSequence += ''.join(dfsNodeList)



    print nodeSequence

    return nodeSequence


#***************************************************
# calculate the edit distance
#***************************************************

def get_sequence():

    start = time.time()

    f=open(pairPath)
    pairLines = f.readlines()

    for line in pairLines:
        line = line.replace("\n","")
        segs = line.split(",")
        oriapk = segs[0]
        repapk = segs[1]

        oriapkPath = os.path.join(oriPath,oriapk)
        repapkPath = os.path.join(repPath,repapk)

        if os.path.exists(oriapkPath) and os.path.exists(repapkPath):
            orif = open(oriapkPath)
            repf = open(repapkPath)

            GL = creategraph(orif.readlines())
            TL = creategraph(repf.readlines())

            oriSeq = dfs(GL)
            repSeq = dfs(TL)

            distance = Levenshtein.distance(oriSeq,repSeq)

            ratio = Levenshtein.ratio(oriSeq,repSeq)

            print oriapk,repapk,str(distance),str(ratio)

            cmd = "echo {0},{1},{2},{3}>>{4}".format(oriapk,repapk,distance,ratio,"edit_distance")
            os.system(cmd)

    
    end = time.time()



    elapse = end - start

    print elapse

    cmd = "echo {0}>>{1}".format(elapse,"edit_distance_time")
    os.system(cmd)


get_sequence()

print "all work is done!"
#print find_lcseque('ABCBDAB','BDCABA')
