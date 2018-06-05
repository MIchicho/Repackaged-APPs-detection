#!/usr/bin/env python
# coding=utf-8
import os

cmd = "echo @relation feature>>FeatureHashData.arff"
os.system(cmd)

cmd = "echo @attribute sha256 string >> FeatureHashData.arff"
os.system(cmd)


for i in range(907):
    vet = 'vector' + str(i)
    cmd = "echo {0} {1} {2} >> {3}".format('@attribute',vet,'numeric','FeatureHashData.arff')
    os.system(cmd)


cmd = "echo @data >> FeatureHashData.arff"
os.system(cmd)


print "all work is done!"
