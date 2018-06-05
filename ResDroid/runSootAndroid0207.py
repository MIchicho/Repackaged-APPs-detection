#!/usr/bin/env python
# coding=utf-8
import os
import sys


print'''
================================================
You can use the default apk files's path or input the path you like!
usage: python runSootAndroid.py 
you need to give the <apk_path-apktool> <Output_path>
Example : python feedQAPKforGator.py 
<apk_path-apktool> : /home/chicho/result/gt/repackaged 
<Output_path> : /home/chicho/result/sootAndroidOut/ 
Input : 0 -> default path
Input : 1 -> you personal path
================================================
'''

input = raw_input("you choice? 0 or 1:\n")

while (input != '0') and ( input != '1' ):
    print "you input is wrong!"
    input = raw_input("you choice? 0 or 1:\n")



if ( input == '0' ):
    print "You choose the default path! ...processing...\n"

    gator_path = "/home/chicho/workspace/repackaged/result/repackaged/"

    outPutpath = "/home/chicho/result/sootAndroidOut/repackaged/"
else:
    gator_path = raw_input("you gator apk Path:\n")
    
    if not os.path.exists(gator_path):
        print "Cannot find the path, please check you input Path!\n"
        sys.exit(1)

    outPutpath = raw_input("you output path:\n")

    

WrongPath = os.path.join(outPutpath,"WrongInfo")

logPath = os.path.join(outPutpath,"LOG")

if not os.path.exists(outPutpath):
    os.makedirs(outPutpath)

if not os.path.exists(logPath):
    os.makedirs(logPath)

if not os.path.exists(WrongPath):
    os.makedirs(WrongPath)


GatorProjPath = os.listdir(gator_path)



i = 0
for project in GatorProjPath:
    Projpath = os.path.join(gator_path,project)
    SootAndroidPath = "/home/chicho/workspace/ResDroid/SootAndroid/scripts/guiAnalysis.sh" 
   # SootAndroidPath = "/home/chicho/tools/gator/gator-3.1/SootAndroid/scripts/guiAnalysis.sh"
    AndroidBench = "/home/chicho/tools/gator/AndroidBench/"
    sdkPath = "/home/chicho/Android/Sdk/"
    #logfilePath = os.path.join(logPath,project+".txt") 

    outfilename = project + ".txt"

    outfilePath = os.path.join(outPutpath,outfilename)

    logfilePath = os.path.join(logPath,outfilename)

    if os.path.exists(logfilePath):
        cmd = "This file ++{0}++ has already exists!\n".format(outfilename)
       # print cmd 
        i = i + 1
        continue
    
    # some important info:
    # outfile has wrong info 
    # LOG file we can get more info includes xml-GUIHierarchy
    print "now handle the {0}".format(project)
    print "..." 
    #cmd = '''sh {0} {1} {2} {3} android-15 /home/chicho/AndroidDemo | grep -v ":" > {4}'''.format(SootAndroidPath,AndroidBench,sdkPath,Projpath,outfilePath)
    cmd = '''SootAndroidOptions="-client Ch5Client -client GUIHierarchyPrinterClient" sh {0} {1} {2} {3} android-15 {4} > {5} 2>&1 >> {6}'''.format(SootAndroidPath,AndroidBench,sdkPath,Projpath,project,outfilePath,logfilePath)
    os.system(cmd)
    print "the {0} has already finished!".format(project)

   
   # moveGUIHier.sh this shell script's function : find if Gator has already generate the xml file 
    cmd = "./moveGUIHier.sh {0} {1}".format(logfilePath,outPutpath)
    os.system(cmd)
    
    
    print "process" + gator_path

    wrongFileSize = os.path.getsize(outfilePath)

    if(wrongFileSize == 0):
        cmd = "rm {0}".format(outfilePath)
        os.system(cmd)
    else:
        cmd = "mv {0} {1}".format(outfilePath, WrongPath)
        os.system(cmd)


    #print "process" + gator_path


'''
xmlList = os.listdir(outPutpath)

wronginfoLogList = os.listdir(WrongPath)

for xmlfile in xmlList:
    if (xmlfile.endswith(".xml")):
        xmlportion = xmlfile.split("-")
        xmlname = xmlportion[0]

    for wrongLog in wronginfoLogList:
        portion = os.path.splitext(wrongLog)
        Log = portion[0]
        if (Log == xmlname):
            wrongLogPath = os.path.join(WrongPath,wrongLog)
            if os.path.exists(wrongLogPath):
                cmd = "rm {0}".format(wrongLogPath)
                os.system(cmd)
                break


'''
tips = "There are {0} apks have already handled!\n".format(i)
print tips 


print "****************************************"
print "all work done!\n"
