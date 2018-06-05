#!/usr/bin/env python
# coding=utf-8
# author    : Chicho 
# date      : 2017-2-9
# function  : 1. use the tool dexdump to decompile the dex file
#             2. get the opcode and store it in a file name apkName.txt
#             3. All of these files are store under the directory Juxtapp
# running   : Two methods
#             1. python parseDexOpcode.py
#             2. python parseDexOpcode.py  your PATH

import os
from random import shuffle


print "Usage:"
print '''
============================================================
running  : python parseDexOpcode.py
You can input different number to choose which path you want 
to use 
************************************************************
input : 0 -> original APKs  ~/workspace/repackaged/result/original/ 
input : 1 -> repackaged APKs ~/workspace/repackaged/result/repackaged/
input : 2 -> test PATH 
input : 3 -> your PATH  
============================================================
'''

print "\n"


input = raw_input("your choice? 0,1,2 or 3:\n")

while (input !='0') and (input != '1') and ( input !='2' ) and (input !='3'):
    print "your input is wrong!"
    input = raw_input("what is your choice? 0,1,2 or 3:\n")


if (input =='0'):
    print "you choose the default original path ...processing..."
    
    Path = "/home/chicho/workspace/repackaged/result/original/"
    outputPath="/home/chicho/workspace/repackaged/Juxtapp/original/"

if (input == '1'):
    print "You choose the default repackaged path！...processing..."

    Path = "/home/chicho/workspace/repackaged/result/repackaged/"
    outputPath="/home/chicho/workspace/repackaged/Juxtapp/repackaged/"



apkList=os.listdir(Path) # to get all the processed apks under the directory 
# shuffle the fixed sequence
shuffle(apkList)




for apk in apkList:
    
    apkfileName = apk+".txt"
    
    # check whether or not the apk has get the opcode file each time
    outputList = os.listdir(outputPath)
    if apkfileName in outputList:
        tips = "{0} file has already existed".format(apk)
        print tips
        continue
    # if this file exists, we can handle others

    apkPath = os.path.join(Path,apk)
    dexpath = os.path.join(apkPath,"bin","classes","classes.dex")

    # check this apk contains classes.dex file 
    if not os.path.isfile(dexpath):
        continue

    #classes.txt is used to store the opcode the middle result
    midFile = os.path.join(apkPath,"bin","classes","classes.txt")

    cmd = "dexdump -d {0} >> {1}".format(dexpath,midFile)
    os.system(cmd)
    
    if not os.path.isfile(midFile):
        print "The file not exists!"
        continue

    if os.path.getsize(midFile)==0:
        print "dexdump cannot parse anything of " + apk
        continue

    tips = "now we are handleding {0}.apk".format(apk)
    print tips

    f = open(midFile)

    for line in f.readlines():
        if "|" in line and ":" in line:
            judgeCode = line.split("|")[1]
            if judgeCode.startswith("["):
                continue
            

            try:
                opcode = line.split("|")[1]
                if " " in opcode:
                    opcode = opcode.split()[1]
                else:
                    continue
            except:
                continue


            print opcode
            if opcode.startswith("const"):
                continue
            
            finalFileName = apk+".txt"
            finalFilePath = os.path.join(outputPath,finalFileName)

            cmd = "echo {0} >> {1}".format(opcode,finalFilePath)
            os.system(cmd)

    f.close()

print "all work is done!"

