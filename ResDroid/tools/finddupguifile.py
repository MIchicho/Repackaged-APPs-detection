#!/usr/bin/env python
# coding=utf-8
import os

path = "/home/chicho/result/sootAndroidOut_19_SHOP/"

guifileList = os.listdir(path)

gui_cnt = len(guifileList)

deleList = []

for i in range(gui_cnt):
    guifile = guifileList[i]
    if guifile.endswith(".xml"):
        guiname1 = guifile.split("-")
        guiname1.pop()

        guiname1 = '-'.join(guiname1)

        for j in range(i+1,gui_cnt):
            if (guifileList[j].endswith(".xml")):
                guiname2 = guifileList[j].split("-")
                guiname2.pop()

                guiname2 = '-'.join(guiname2)

                if (guiname1 == guiname2):
                    deleList.append(guifileList[j])




for gui in deleList:
    guiPath = os.path.join(path,gui)
    cmd = "rm {0}".format(guiPath)
    os.system(cmd)
    print cmd 


