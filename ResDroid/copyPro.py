#!/usr/bin/env python
# coding=utf-8
# filename : copyPro.py
# author   : chicho 
# function : this file is  find has handled apk by feedQAPKforGator.py and copy project.properties to the apkfile(apktool and dex2jar) 




import os 
import sys

if(len(sys.argv)==3):
    path = sys.argv[1]
    proPath = sys.argv[2]

if(len(sys.argv)<3):
    print'''
    ================================================
    You can use the default apk files's path or input the path you like!
    usage: python feedQAPKforGator.py <apk_path> <Output_path>
    Example : python copyPro.py /home/chicho/result/36/APK_36_WEATHER/ /home/chicho/result/project.properties 
    Input : 0 -> default path
    Input : 1 -> you personal path
    ================================================
    '''



    input = raw_input("you choice ? 0 or 1:\n")

    while (input != '0') and (input != '1'):
        print "you input is wrong!"
        input = raw_input("you choice? 0 or 1:\n")

    if (input == '0'):
        print "you choose the default path! ...processing...\n"
        
        path = "/mnt/grace/result/APK_12_TRA6/"
        proPath = "/home/ubuntu/project.properties"
    else:
        path = raw_input("you apktool_out path:\n")
        #judge you input apk_path right
        if not os.path.exists(path):
            print "Cannot find the path, please check you input path!:p\n"
            sys.exit(1)

        proPath = raw_input("you project.properties path: \n")






apkFileList=os.listdir(path)

for apk in apkFileList:
    apk_Path = os.path.join(path,apk)

    cmd = "cp {0} {1}".format(proPath,apk_Path)
    #os.system(cmd)
    
    tips = "now cope {0} to {1}".format("project.properties",apk_Path)
    print tips 
    
    cmd = "echo {0} >>~/apkList12.txt".format(apk)
    os.system(cmd)

print "all work done!\n"
