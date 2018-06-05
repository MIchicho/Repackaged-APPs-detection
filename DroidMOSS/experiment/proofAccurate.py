#!/usr/bin/env python
# coding=utf-8
#  Author   :  Chicho
#  Date     :  2017-05-03
#  Function :  1. match the result in dir /code/experiment/pair2.txt
#               weather is right with the file repackaging_pairs.txt

import os


gtPath = "/home/chicho/workspace/repackaged/repackaging_pairs.txt"

rePath = "/home/chicho/workspace/repackaged/DroidMOSS/code/experiment/pair2.txt"


# find the not match pair2.txt

gtf = open(gtPath)

refile = open(rePath)

gtAPKPairs = gtf.readlines()

refilePairs = refile.readlines()

# find the not match pairs
for gtpair in gtAPKPairs:

    if gtpair not in refilePairs:
        gtpair = gtpair.replace("\n","")
        cmd = "echo {0} >> {1}".format(gtpair,"notMatch.txt")
        os.system(cmd)

        print gtpair + " not match..."


# find the match pairs 
print "***************************"
for parsePair in refilePairs:

    parsePair = parsePair.replace("\n","")

    cmd = ''' egrep "{0}" {1} >> {2}'''.format(parsePair,gtPath,"match.txt")

    #os.system(cmd)

    #print parsePair + " is the match pairs!"

gtf.close()
refile.close()

print "all work is done!..."

