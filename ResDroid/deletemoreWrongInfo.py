#!/usr/bin/env python
# coding=utf-8
import os
 

path = "/home/chicho/result/"

fileList = os.listdir(path)

for sootfile in fileList:
    if (sootfile.startswith('sootAndroidOut')):
        outPath = os.path.join(path,sootfile)
        wrongpath = os.path.join(outPath,"WrongInfo")

        xmlList = os.listdir(outPath)

        wrongLogList = os.listdir(wrongpath)


        leninfo=len(wrongLogList)
        i=0
        for Log in wrongLogList:
            portion = os.path.splitext(Log)
            logFile = portion[0].split("-")[-1]
            #print "logFile",logFile
            #LogPath = os.path.join(wrongpath,Log)
            for xmlfile in xmlList:
                if (xmlfile.endswith(".xml")):
                    try:
                        xmlname = xmlfile.split("-")[-2]
                    except:
                        print xmlfile
                        
                        
                    if (xmlname == logFile):
                        LogPath = os.path.join(wrongpath, Log)
                        if os.path.exists(LogPath):
                            cmd = "rm {0}".format(LogPath)
                            os.system(cmd)
                            print "delete the {0} file.".format(Log)
                            i = i+1
                            break


        cmd =  "There are {0},and delete {1} files".format(leninfo,i)


print "all work done!"
