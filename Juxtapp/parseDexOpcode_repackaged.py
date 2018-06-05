#!/usr/bin/env python
# coding=utf-8
import os

Path = "/home/chicho/workspace/repackaged/result/repackaged/"

apkList=os.listdir(Path)

outputPath="/home/chicho/workspace/repackaged/Juxtapp/repackaged/"

outputList=os.listdir(outputPath)

for apk in apkList:

    apkfileName = apk+".txt"

    if apkfileName in outputList:
        tips = "{0} file has aleardy existed".format(apk)
        print tips

    apkPath = os.path.join(Path,apk)
    dexpath = os.path.join(apkPath,"bin","classes","classes.dex")

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
    print tips
    print tips


    f = open(midFile)

    for line in f.readlines():
        if "|" in line and ":" in line:
            judgeCode = line.split("|")[1]
            if judgeCode.startswith("["):
                continue
            
            # some lines may not contains spaces
            try:
                opcode = line.split("|")[1]
                if " " in opcode:
                    opcode =opcode.split()[1]
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
