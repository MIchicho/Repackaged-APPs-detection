#!/usr/bin/env python
# coding=utf-8
# Author   :  Chicho
# Date     :  2017-10-05
# Running  :  python findDialog.py


import os


print "Usage:"


print '''
=========================================================
running  :  python findDialog.py
********************************************************
input : 0 -> original APKs
input : 1 -> repackaged APKs
input : 2 -> test Path
=========================================================
'''

print "\n"


input = raw_input("your choice 0 or 1 or 2:\n")


while (input != '0') and (input!='1') and (input!='2'):
    print "your input is wrong!"
    input = raw_input("your choice 0 or 1 or 2:\n")


if (input == '0'):
    path = "/home/chicho/workspace/repackaged/result/original/"

if (input == '1'):
    path = "/home/chicho/workspace/repackaged/result/repackaged/"

num = 0 
flagFind = "False"

def findDialog(path):
        
    num = 0 
    flagFind = "False"
    apkList = os.listdir(path)

    for apk in apkList:
        count = 0
        apkPath = os.path.join(path,apk)
        samliPath = os.path.join(apkPath,"smali")

        for root,dirs,files in os.walk(samliPath):

            for file in files:
                fPath = os.path.join(root,file)

                fp = open(fPath)

                flines = fp.readlines()

                for line in flines:
                    if "AlertDialog" in line:
                        flagFind = "True"
                        num +=1
                        count +=1
                        break

                    if "DialogFragment" in line:
                        count +=1


                if flagFind == "True":
                    print apk + " " + str(count)
                    break

                

            if flagFind == "True":
                flagFind = "False"
                break



         
        print num 
    
    print num 
    print num 



findDialog(path)


print "all work is done!"



