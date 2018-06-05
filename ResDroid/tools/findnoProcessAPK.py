#!/usr/bin/env python
# coding=utf-8
import os
import sys

print'''
================================================
You can use the default apk files's path or input the path you like!
usage: python findnoProcess.py <apk_path> <forgator_path>
Example : python feedQAPKforGator.py /home/chicho/test/APK /home/chicho/test/Output_path
Input : 0 -> default path
Input : 1 -> you personal path
================================================
'''



input = raw_input("you choice ? 0 or 1:\n")

while (input != '0') and (input != '1'):
    print "you input is wrong!"
    input = raw_input("you choice ? 0 or 1:\n")

if (input == '0'):
    print "you choose the default path! ...processing...\n"

    path = "/media/chicho/567310cf-0c8f-45a1-9ef3-a372e22cec0c/yuru/GooglePlayApps/ByCategory/1_ARCADE"

    gator_path = "/home/chicho/result/APK"
else:
    path = raw_input("you APK path:\n")
    #judge you input apk_path right
    if not os.path.exists(path):
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)
    
    
    gator_path = raw_input("you path will be process by Gator: \n")
    if not os.path.exists(gator_path): 
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)


apktoolList = os.listdir(gator_path)

APKList = os.listdir(path)

output = "/home/chicho/Workspace/ResDroid/find/"

baseName = os.path.basename(path)

Output_path = os.path.join(output,baseName)
print Output_path


j=0
k=0
m=0
for APK in APKList:
    k = k+1
    if ( APK.endswith(".apk")):
        
        portion = os.path.splitext(APK)

        apkname = portion[0]
        
        i = 0;
        for apkfile in apktoolList:
            m = m+1
            if( apkfile == apkname ):
                break
            i = i + 1

        if (i==len(apktoolList)):
            APK_Path = os.path.join(path,APK)
            if not os.path.exists(Output_path):
                os.makedirs(Output_path)
                print Output_path
            cmd = "cp {0} {1}".format(APK_Path,Output_path)
            os.system(cmd)
            tip  = "find no process APK ->{0}".format(APK)
            print tip
            j = j+1
    


if (j == 0):
    print "all APKs have processed!"



print k
print len(apktoolList)
print "all work done!"

