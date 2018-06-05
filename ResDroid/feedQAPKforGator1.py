#!/usr/bin/env python
# coding=utf-8

import os
import sys
import zipfile


print'''
================================================
You can use the default apk files's path or input the path you like!
usage: python feedQAPKforGator.py <apk_path> <Output_path>
Example : python feedQAPKforGator.py /home/chicho/test/APK /home/chicho/test/Output_path
Input : 0 -> default path
Input : 1 -> you personal path
================================================
'''


# the path stores the apks
# the apks handled by apktool and dex2jar.sh will be store in the 
#gator_path

input = raw_input("you choice ? 0 or 1:\n")

while (input != '0') and (input != '1'):
    print "you input is wrong!"
    input = raw_input("you choice ? 0 or 1:\n")

if (input == '0'):
    print "you choose the default path! ...processing...\n" 
    path = "/home/chicho/workspace/repackaged/pairs/repackaging/"
    gator_path = "/home/chicho/workspace/repackaged/result/repackaged/"
else:
    path = raw_input("you APK path:\n")
    #judge you input apk_path right
    if not os.path.exists(path):
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)

    gator_path = raw_input("you Output_path: \n")




if not os.path.exists(gator_path):
    os.makedirs(gator_path)

apklist = os.listdir(path)


for APK in apklist:
    #P = os.path.join(path,APK)
    if APK.endswith(".apk"):
        portion = os.path.splitext(APK)
        
        outputAPKfile = os.path.join(gator_path,portion[0])
        
        if os.path.exists(outputAPKfile):
            tips = "The file **{0}** has already exists!".format(portion[0])
            print tips
            continue


        # rename
        if portion[1] == ".apk":
            newname = portion[0] + ".zip"
            
            apkPath = os.path.join(path,APK)
            newPath = os.path.join(path,newname)
           # os.rename(apkPath,newPath)

        apkname = portion[0]


        # create a path to store each apks
        gator_apk_path = os.path.join(gator_path,apkname) #e.g. /home/chicho/result/APK/<apklist> 
        
        
        cmd = "apktool d {0} -o {1}".format(apkPath,gator_apk_path)
        os.system(cmd)
        

        os.rename(apkPath,newPath)

        if not os.path.exists(gator_apk_path):
            os.makedirs(gator_apk_path)

        zip_apk_file = os.path.join(path,newname) # get the zip files

        if not os.path.exists(zip_apk_file):
            continue
        
        try:
            z = zipfile.ZipFile(zip_apk_file, 'r')
        except Exception:
            continue

        for filename in z.namelist():
            '''
            if filename == "AndroidManifest.xml":
                manifestPath = os.path.join(gator_apk_path, "Manifest.xml")
                f = open(manifestPath, 'w+')
                
                f.write(z.read(filename))
                f.close()

               # time.sleep(1)
            
                

                # make AndroidManifest.xml readable
                AXMLPath = "/home/chicho/tools/Androidtools/AXMLPrinter2.jar"
                newmanifestPath = os.path.join(gator_apk_path,filename)
                cmd1 = "java -jar {0} {1} > {2}".format(AXMLPath,manifestPath,newmanifestPath)
                os.system(cmd1)

               # time.sleep(1)
                

                cmd2 = "rm {0}".format(manifestPath)
                os.system(cmd2)

               # time.sleep(1)
            '''

            if filename.endswith(".dex"):
                dexfile = "classes.dex"
                classPath = os.path.join(gator_apk_path,"bin/classes")
                if not os.path.exists(classPath):
                    os.makedirs(classPath)

                dexfilepath = os.path.join(classPath,dexfile)
                f = open(dexfilepath, 'w+')
                f.write(z.read(filename))
                f.close()

               # time.sleep(2)
                os.chdir(classPath)
                cmd = "dex2jar.sh {0}".format(dexfilepath)
                os.system(cmd)
		
		
               # jarPath = os.path.join(classPath,"classes_dex2jar.jar")
                
                os.chdir(classPath)
                try:
                    cmd = "unzip classes-dex2jar.jar"
                    os.system(cmd)
                except:
                    pass
                        

                cmd = "rm classes-dex2jar.jar"
               # os.system(cmd)

                smaliPath = os.path.join(gator_apk_path,"smali")
               # cmd = "rm -r {0}".format(smaliPath)
                #os.system(cmd)

                ymlPath = os.path.join(gator_apk_path,"apktool.yml")
                cmd = "rm {0}".format(ymlPath)
               # os.system(cmd)


                os.chdir(gator_apk_path)
		
                # cp the project.properties ~/result/APK/***
                propertyPath = "/home/chicho/result/project.properties"
                cmd = "cp {0} {1}".format(propertyPath,gator_apk_path)
                os.system(cmd)
           	
        os.rename(newPath,apkPath)
    else:
        continue



print path 
print gator_path 

print "...\n"
print "all work done!\n"
