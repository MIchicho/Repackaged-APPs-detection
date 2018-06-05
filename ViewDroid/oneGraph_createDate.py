#!/usr/bin/env python
# coding=utf-8
# author   : Chicho 
# date     : 2016-10-28
# function : 1. parse the AndroidManifest.xml file 
#               this file is handled by feedQAPKforGator.py
#               which are handled by apktool and dex2jar.sh 
#               so we need to install the apktool and dex2jar.sh
#            2. parse the satg and construct the ATG the number is beginning
#               from the MainActivity. If the apk has not MainActivity
#               we parse the APK from the first satg.xml
#            3. print the result 


import os 
import sys
import xml.dom.minidom


print "Usage:"
print'''
==============================================
running : python createData.py
you can input different number to choose the different PATH
*********************************************
input : 0 -> original APKs
input : 1 -> repackaged APKs
input : 2 -> test PATH 
input : 3 -> your PATH 
=============================================
'''



# when we meet some special apps we cp the special app into this path 
deep_analysisPath="/home/chicho/workspace/repackaged/result/deep_analysis/"

print "\n"

input = raw_input("you choice? 0 or 1 or 2:\n")

while (input != '0') and (input != '1') and ( input != '2' ):
    print "you input is wrong!"
    input = raw_input("you choice? 0 or 1 or 2:\n")



if (input == '0'):
    print "you choose the original path!....processing...."

    APKPath="/home/chicho/workspace/repackaged/result/original/"  # the APK PATH is the APK have handled by apktool
    satgPath="/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/"
    outPutpath = "/home/chicho/workspace/repackaged/data/OrignalDB"
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/graph/original/"

if (input == '1'):
    print "you choose the repackaged path! ....processing...."

    APKPath = "/home/chicho/workspace/repackaged/result/repackaged/"
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/"
    outPutpath = "/home/chicho/workspace/repackaged/data/RepackagedDB"
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/graph/repackaged/"

if (input == '2'):
    print "you choose the test path! ....processing...."

    APKPath = "/home/chicho/test/problem_Test/apk/"
    satgPath = "/home/chicho/test/problem_Test/satg/"
    outPutpath = "/home/chicho/test/problem_Test/testDB"
    graphPath = "/home/chicho/test/problem_Test/graphDB"


if (input == '3'):

    APKPath = raw_input("you apk PATH:\n")

    satgPath = raw_input("you satg PATH:\n")

    if not (os.path.exists(APKPath) or os.path.exists(satgPath)):
        print "CANNOT find the PATH, please check your input!"
        sys.exit(1)

    outPutpath = raw_input("your dataSet for VF2 PATH:\n")

    graphPath = raw_input("your graph note PATH:\n")

'''
if input == 0:
    wrongFileLog="/home/chicho/workspace/repackaged/data/WrongInfo_or"
    noEdge = "/home/chicho/workspace/repackaged/data/originalnoEdge"
    
if input == 1:
    wrongFileLog = "/home/chicho/workspace/repackaged/data/WrongInfo_re"
    noEdge = "/home/chicho/workspace/repackaged/data/repackagednoEdge"

    print "input here"
'''

#**********************************************
# We parse the AndroidManifest.xml file 
# and find the MainActivity
#**********************************************
def findMainActivity(manifestPath):
    
    print "we are in findMainActivity"

    findflag = 0
    MainActivity = ""
    actCnt=0
    package=""

    if not os.path.exists(manifestPath): 
        return (findflag,MainActivity,actCnt,package)
   
    
    try:
        dom = xml.dom.minidom.parse(manifestPath)
    except: 
        return (findflag,MainActivity,actCnt,package)

    root = dom.documentElement

    actList = root.getElementsByTagName('activity')


    actCnt = len(actList)
    print "actCnt " + str(actCnt)

    package = root.getAttribute('package')

    for activity in actList:
       # actName = activity.getAttribute('android:name')

        # delete the ads
    #    if '.' in actName and not actName.startswith('.') \
    #       and not actName.startswith(package):
    #        actCnt = actCnt - 1

        if activity.toxml().find("android.intent.action.MAIN")>0\
           and activity.toxml().find("android.intent.category.LAUNCHER")>0:
            findflag=1
            MainActivity = activity.getAttribute('android:name')


            if MainActivity.startswith("."):
                package=root.getAttribute('package')
                MainActivity=package+MainActivity

            if not '.' in MainActivity:
                MainActivity = package + "." + MainActivity


    
    return (findflag,MainActivity,actCnt,package)


#
#**************************************************
# get all the nodes and the Edge  
# parse the satg 
# Create the ATG 
#**************************************************

def getTheEdgeSet(manifestPath,apkSatgPath):

    print "we are in the getTheEdgeSet"

    findflag, MainActivity,actCnt,package=findMainActivity(manifestPath)

    print "findflag: " + str(findflag)
    print "MainActivity: " + MainActivity
    print "Activity count: " + str(actCnt)

    print "package name: " + package


    EdgeCollection = []
    
    edgeDict = {}

    parentActNameCollection = []
    
    if not os.path.exists(apkSatgPath):
        return (EdgeCollection,edgeDict,parentActNameCollection)


    try:
        dom = xml.dom.minidom.parse(apkSatgPath)
    except:
        return (EdgeCollection,edgeDict,parentActNameCollection)

    root = dom.documentElement

    parentActList = root.getElementsByTagName('Activity')

   # EdgeCollection = []
    # edgeDict= {}
    
    startIndex=0

    
    # delete the ads
    portion = package.split(".")

    if len(portion) == 3:
        del portion[-1]
    elif len(portion) > 3:
        del portion[-1]
        del portion[-2]
    elif len(portion) <= 2:
        pass

    package = '.'.join(portion)

    # we should pay attention the package name may not is 
    #the same with some activity 
    # In this situation, we should use the MainActivity's prefix 

    if findflag ==1:
        if not MainActivity.startswith(package):

            portion = MainActivity.split(".")

            del portion[-1]

            package = '.'.join(portion)

    # delete the ad libraries
    tmpEdgeSetList=[]
    tmpParentList = []
    for activity in parentActList:
        actName = activity.getAttribute('name')

        if not actName in tmpParentList:
            tmpParentList.append(actName)
        
        if not actName in tmpEdgeSetList:
            tmpEdgeSetList.append(actName)
        
        childActList = activity.getElementsByTagName('ChildActivity')
        
        for child in childActList:
            childName = child.getAttribute('name')

            if not childName in tmpEdgeSetList:
                tmpEdgeSetList.append(childName)
    
    # some ads' activity only need to declare the main in Manifest file 
    # but when we use the static to generate the ATG we can find the 
    # ads has more edge (Activity) in the graph ATG so we need to reflash
    # the count of the activity 
    # if the A3E can get more Activity we should use the larger number

    
    if actCnt < len(tmpEdgeSetList):
        actCnt = len(tmpEdgeSetList)
    
    print "The satg edge number is :" + str(len(tmpEdgeSetList))
    for actName in tmpEdgeSetList:
        if not actName.startswith(package):
            actCnt = actCnt - 1
            print "inconformity Activity :" + actName


    # something wrong for the satg parsing 
    if not MainActivity in tmpEdgeSetList:
        findflag = 0

    if not MainActivity in tmpParentList:
        findflag = 0

    print "The final Activity count: " + str(actCnt)

    # in some situation the A3E cannot parse the apk 
    # but we also find the APK has activity 
    # in this situation we need deep analysis about this situation
    # actCnt !=0 which means has activities
    # that means the A3E cannot parse any node
    # we only consider the number of nodes are larger than 2
    # deep_analysisPath="/home/chicho/workspace/repackaged/result/deep_analysis/"
   
    if input == '0':
        noparsePath = "/home/chicho/workspace/repackaged/data/noParse_or1"
    elif input == '1':
        noparsePath = "/home/chicho/workspace/repackaged/data/noParse_re1"

    if actCnt != 0 and len(tmpEdgeSetList) == 0 and actCnt > 2:
        eachsatgPath = os.path.split(apkSatgPath)[-1]
        apkname = eachsatgPath.split(".")
        cmd = "echo {0} >> {1}".format(apkname,noparsePath)
        os.system(cmd)

    '''
    if actCnt != 0 and len(tmpEdgeSetList)==0 and actCnt >2:
        eachapkPath,manifile = os.path.split(manifestPath)
        decomAnalysisPath = os.path.join(deep_analysisPath,"noparse","APKs_decompile")
        if not os.path.exists(decomAnalysisPath):
            os.makedirs(decomAnalysisPath)
        cmd = "cp -r {0} {1}".format(eachapkPath,deep_analysisPath)
        os.system(cmd)
        satgAnalysispath = os.path.join(deep_analysisPath,"satg")
        if not os.path.exists(satgAnalysispath):
            os.makedirs(satgAnalysispath)

        cmd = "cp {0} {1}".format(apkSatgPath,satgAnalysispath)
        os.system(cmd)
    '''



    #MainActivity
    if findflag==1:
        EdgeCollection.append(MainActivity)

        for i in range(actCnt):

            print "i " + str(i)

            for activity in parentActList:
                parentName = activity.getAttribute('name')

                if not parentName.startswith(package):
                    continue


                childNameList = []

                if parentName == EdgeCollection[startIndex]:

                    if parentName not in parentActNameCollection:
                        parentActNameCollection.append(parentName)

                    childActList = activity.getElementsByTagName('ChildActivity')

                    for child in childActList:
                        childName = child.getAttribute('name')

                        if childName not in childNameList:
                            childNameList.append(childName)

                        if childName not in EdgeCollection:
                            EdgeCollection.append(childName)

                    edgeDict[parentName]=childNameList


                    break
            
            print "startIndex " + str(startIndex)

            print "len EdgeCollection" + str(len(EdgeCollection))

            # if the programme run here that means the graph 
            # is discontinuous
            # in this situation we need to deep analysis
            disconPath="/home/chicho/workspace/repackaged/data/discon_repackaged1"
            eachsatgPath = os.path.split(apkSatgPath)[-1]
            cmd = "echo {0} >> {1}".format(eachsatgPath,disconPath)
            os.system(cmd)


            '''
            eachapkPath,manifile = os.path.split(manifestPath)
            decomAnalysisPath = os.path.join(deep_analysisPath,"discontinuous","APKs_decompile")
            if not os.path.exists(decomAnalysisPath):
            	os.makedirs(decomAnalysisPath)
            cmd = "cp -r {0} {1}".format(eachapkPath,decomAnalysisPath)
            os.system(cmd)

            satgAnalysispath = os.path.join(deep_analysisPath,"discontinuous","satg")
            if not os.path.exists(satgAnalysispath):
                os.makedirs(satgAnalysispath)

            cmd = "cp {0} {1}".format(apkSatgPath,satgAnalysispath)
            os.system(cmd)
            '''

        #    if len(EdgeCollection) == actCnt:
        #        break

            if startIndex < len(EdgeCollection)-1:    
                startIndex = startIndex + 1

          
        #    if startIndex >= actCnt-1:
        #        break

        
    elif findflag==0:

        for activity in parentActList:
            actName = activity.getAttribute('name')

            if not actName.startswith(package):
                continue
            
            if actName not in parentActNameCollection:
                parentActNameCollection.append(actName)

            childNameList=[]

            if actName not in EdgeCollection:
                EdgeCollection.append(actName)


            childActList = activity.getElementsByTagName('ChildActivity')

            
            for child in childActList:
                childName = child.getAttribute('name')
                if childName not in childNameList:
                    childNameList.append(childName)

                if childName not in EdgeCollection:
                    EdgeCollection.append(childName)


            edgeDict[actName]=childNameList


    return (EdgeCollection,edgeDict,parentActNameCollection)





#*************************************
#  print the result 
#*************************************
def createData(manifestPath,apkSatgPath,index,apk_satgFile):

    print "we are in createData"
    
    EdgeCollection,edgeDict,parentActNameCollection=getTheEdgeSet(manifestPath,apkSatgPath)

    print EdgeCollection

    print edgeDict

    print parentActNameCollection

    apkname = apk_satgFile.split(".")[0] + ".txt"
    apkoutPutPath = os.path.join(graphPath,apkname)

    
    if input == '0':
        wrongFileLog="/home/chicho/workspace/repackaged/data/WrongInfo_or1"
        noEdge = "/home/chicho/workspace/repackaged/data/originalnoEdge1"
    
    if input == '1':
        wrongFileLog = "/home/chicho/workspace/repackaged/data/WrongInfo_re1"
        noEdge = "/home/chicho/workspace/repackaged/data/repackagednoEdge1"

    

    if len(EdgeCollection)==0:# wrongFileLog stores the apps without nodes
        cmd = '''echo "this graph has not any node" {0} {1} >> {2}'''.format(index,apkname,wrongFileLog)
        os.system(cmd)
        cmd = "echo {0} >> {1}".format(apk_satgFile,wrongFileLog)
        os.system(cmd)
        return

    if len(edgeDict)==0:
        cmd = "echo this graph has not and edge: {0} {1}>> {2}".format(index,apkname,noEdge)
        os.system(cmd)
        cmd = "echo {0} >> {1}".format(apkname,wrongFileLog)
        os.system(cmd)
        return 

    
    if len(EdgeCollection)==1:
        pass 

    cmd='''echo "t #" {0} >> {1}'''.format(index,outPutpath)
   # os.system(cmd)


    cmd='''echo "t #" {0} {1}>> {2}'''.format(index,apkname,graphPath)
   # os.system(cmd)

    for vex in range(len(EdgeCollection)):
        cmd = "echo v {0} >> {1}".format(vex,outPutpath)
      #  os.system(cmd)

    
    for key in parentActNameCollection:
        tmpList = edgeDict[key]

        for child in tmpList:
            sourceName = key
            targetName = child 

            source = EdgeCollection.index(sourceName)
            target = EdgeCollection.index(targetName)

            print "e " + sourceName + " --> " + targetName
            print "e " + str(source) + " --> " + str(target)

            cmd = "echo {0} {1} >> {2}".format(source,target,apkoutPutPath)
            os.system(cmd)




if __name__ == '__main__':
    
    APKList = os.listdir(APKPath)
    
    index = 0 

    for apk in APKList:
        eachApkPath = os.path.join(APKPath,apk)

        manifestPath = os.path.join(eachApkPath,"AndroidManifest.xml")

        apk_satgFile = apk + ".apk.g.xml"

        apkSatgPath = os.path.join(satgPath,apk_satgFile)

        print "********************"

        print apk_satgFile 

        createData(manifestPath,apkSatgPath,index,apk_satgFile)
        
        index = index + 1
        
    cmd = '''echo "t #" -1>>{0}'''.format(outPutpath)
  #  os.system(cmd)
    print "all work is done!"





