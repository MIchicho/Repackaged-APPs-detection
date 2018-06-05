#!/usr/bin/env python
# coding=utf-8
import os

origPath = "/home/chicho/result/gt/sootAndroidOut/origapps/"

repackagePath = "/home/chicho/result/gt/sootAndroidOut/repackaged/"

origxml = os.listdir(origPath)

repackagedxml = os.listdir(repackagePath)

origOut = "/home/chicho/result/gt/diff/origapps"

repackageOut = "/home/chicho/result/gt/diff/repackaged"

if not os.path.exists(origOut):
    os.makedirs(origOut)


if not os.path.exists(repackageOut):
    os.makedirs(repackageOut)



for origfile in origxml:
    if (origfile.endswith(".xml")):
        orig = origfile.split("-")[-2]

        #print orig

        for repckg in repackagedxml:
            if (repckg.endswith(".xml")):
                repckgName = repckg.split("-")[-2]
                
                #print orig, repckgName
                if ( orig == repckgName ):
                    origFilePath = os.path.join(origPath, origfile)
                    repckFilePath = os.path.join(repackagePath,repckg)
                    # cp the origPath APK
                    cmd = "cp {0} {1}".format(origFilePath,origOut)
                    os.system(cmd)

                
                    cmd1 = "cp {0} {1}".format(repckFilePath,repackageOut)
                    os.system(cmd1)
                    
                    tips = "now move {0}".format(origfile)
                    print tips  
                    break 



print "all work done!"
