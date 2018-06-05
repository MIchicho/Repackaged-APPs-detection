#!/usr/bin/env python
# coding=utf-8
#  Author   :  Chicho 
#  Date     :  2017-06-26
#  filename :  createATGraph.py
#  Version  :  2.0
#  function :  1. parse the AndroidManifest.xml file which is handled by feedQAPKforGator.py
#               the apks are handled by apktool and dex2jar.sh so we should install the apktool and dex2jar.sh
#              2. parse the satg and construct the ATG the number is begin from the MainActivity
#                 If the apk has not MainActivity we parse the APK according to the weight of the Vex 
#                 if a graph has many vex and edge we set a high weight for the parent activity
#              3. we delete the ads
#              4. we output the result

#****  the file format  ******

# F578BHJJGBJK.txt
#t0
#0 1
#0 2
#0 3
#0 4
#t1
#0 1
#0 2
'''
t0
0 1
0 2
0 3
0 4
t1
0 1
0 2
'''

'''
@ in an APK we may get  lots of small graph or a whole graph 
@ some split graphs because the ads some because the a3e cannot
parse the apk correct
'''

# some important things we should consider
# some app has MainActivity but some have not
# the AndroidManifest.xml contains the number of activities may be different from the result of a3e 
# some special situation
# we should consider 0->1 2->1 3->1 4->1 5->1 6->1
#

# special situation:
# we should conside 0->1 1->2 2->3 
#  EdgeCollection  记录顺序，是一个有序的序列 解析完一个parent 之后紧跟着children
# 依次添加进去
# edgeDict 记录着边和边的关系
# 解析出的结果用于保存为文档以APK的 sha256 命名




import os
import sys
import xml.dom.minidom
import operator


print "Usage:"
print '''
============================================================
running : python createATGraph.py
you can input different number to choose the different path 
************************************************************
input : 0 -> original APKs 
input : 1 -> repackaged APKs 
input : 2 -> test PATH 
input : 3 -> your PATH 
============================================================
'''


print "\n"

input = raw_input("you choice? 0 or 1 or 2 or 3:\n")

while (input != '0') and (input != '1') and (input !='2') and (input != '3'):
    print "your input is wrong!"
    input = raw_input("you choice? 0 or 1 or 2:\n")



if (input == '0'):
    print "you choose the original path! ....processing... "

    APKPath = "/home/chicho/workspace/repackaged/result/original/" # the APK PATh is the APK have handled by apktool
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/original/xml/"
    outputPath = "/home/chicho/workspace/repackaged/ViewDroid/updateResult/originalANALYSIS.txt"
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/updateResult/original/"

if (input == '1'):
    print "you choose the repackaged path! ....processing..."

    APKPath = "/home/chicho/workspace/repackaged/result/repackaged/"
    satgPath = "/home/chicho/workspace/ResDroid/a3e-master/apks/repackaged/xml/"
    outputPath = "/home/chicho/workspace/repackaged/ViewDroid/updateResult/repackagedANALySIS.txt"
    graphPath = "/home/chicho/workspace/repackaged/ViewDroid/updateResult/repackaged/"

    
if (input == '2'):
    print "you chooose the test path! ....processing..."

    APKPath = "/home/chicho/test/problem_Test/apk/"
    satgPath = "/home/chicho/test/problem_Test/satg/"
    outputPath = "/home/chicho/test/problem_Test/parseResult.txt"
    graphPath = "/home/chicho/test/problem_Test/"




if (input == '3'):

    APKPath = raw_input("your apk path:\n")

    satgPath = raw_input("your satg path:\n")

    if not (os.path.exists(APKPath) or os.path.exists(satgPath)):
        print "CANNOT find the PATH, please chech your input!"
        sys.exit(1)


    outputPath = raw_input("your detail processing records path\n")

    graphPath = raw_input("your graph path")




#******************************************
# We parse the AndroidManifest.xml file 
# and find the MainActivity
#******************************************



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



def recordFun():

    if (input=='0'):
        pass
#
#*************************************
# get all the nodes and the Edge 
# parse the satg
# Create the ATG
#*************************************




def getTheEdgeSet(manifestPath,apkSatgPath):

    print "We are in the getTheEdgeSet"

    findflag,MainActivity,actCnt,package = findMainActivity(manifestPath)
    
    print "*********************"

    print "findflag: " + str(findflag)
    print "MainActivity: " + MainActivity
    print "package: " + package 
    print "The numbers of activities of AndroidManifest.xml " + str(actCnt)

    cmd = '''echo "findflag: " {0} >>{1}'''.format(findflag,"parseResult.txt")
    os.system(cmd)

    cmd = '''echo "MainActivity: " {0} >>{1}'''.format(MainActivity,"parseResult.txt")
    os.system(cmd)

    cmd = '''echo "package Name: " {0}>>{1} '''.format(package,"parseResult.txt")
    os.system(cmd)

    cmd = '''echo "activity count: " {0} >>{1}'''.format(actCnt,"parseResult.txt")
    os.system(cmd)

    cmd = '''echo "findflag: " {0} >> {1}'''.format(findflag,outputPath)
    os.system(cmd)

    cmd = '''echo "MainActivity: " {0} >>{1}'''.format(MainActivity,outputPath)
    os.system(cmd)

    cmd = '''echo "package: " {0} >> {1}'''.format(package,outputPath)
    os.system(cmd)

    cmd = '''echo "actCnt: " {0} >>{1}'''.format(package,outputPath)
    os.system(cmd)

    
    

    EdgeCollection=[]
    edgeDict={}
    parentActNameCollection=[]

    if not os.path.exists(apkSatgPath):
        print "The satg file not exists."
        return (EdgeCollection,edgeDict,parentActNameCollection)


    ##################
    # the format of satg
    # <ActivityGraph>
    #   <Activity name = "com.anddoes.launcher">
    #       <ChildActivity name = "com.anddoes.launcher" />  # the same name with the Activity
    #       <ChildActivity name = "com.anddoes.launcher2.launcher" event_handler="click" />
    #       <ChildActivity name = "com.anddoes.launcher2.launcher" event_handler="double_click" />
    #       <ChildActivity name = "com.anddoes.APxService">
    #   </Activity>
    # </ActivityGraph>

    # in the satg graph the children's name maybe the same we don't consider the difference among the event_handler
    # we just use a childName 

    try:
        dom = xml.dom.minidom.parse(apkSatgPath)
    except:
        return (EdgeCollection,edgeDict,parentActNameCollection)

    root = dom.documentElement

    ###############

    parentActList = root.getElementsByTagName('Activity') # here empty objects EdgeCollection=[] edgeDict=[] parentActNameCollection=[]

    weightDict={}

    tmpVexList = []

#    here the main purpose is to construct the edgeDict (the relationship between parent and children)
    for activity in parentActList:
        parentName = activity.getAttribute('name')
        
        # delete the ads 
        if parentName.startswith('com.google.ads'):
            continue 

        if parentName.startswith('com.admob.android'):
            continue

        if parentName.startswith('com.umeng'):
            continue
        
        if parentName.startswith('com.inmobi'):
            continue

        if parentName.startswith('com.yume'):
            continue

        if parentName.startswith('com.adview'):
            continue

        if parentName.startswith('com.kiwi.ads'):
            continue

        if parentName.startswith('com.pontilex'):
            continue

        if parentName.startswith('com.adsdk'):
            continue

        if parentName.startswith('com.gfan.sdk'):
            continue

        
        if not parentName in parentActNameCollection:
            parentActNameCollection.append(parentName)

        if not parentName in tmpVexList:
            tmpVexList.append(parentName)

        '''
        if not parentName in EdgeCollection:
            EdgeCollection.append(parentName)
        ''' 

        childNameList = []

        childActList = activity.getElementsByTagName('ChildActivity')

        for child in childActList:
            childName = child.getAttribute('name')
            if not childName in childNameList:
                childNameList.append(childName)

            if not childName in tmpVexList:
                tmpVexList.append(childName)

        if not parentName in edgeDict.keys():
            edgeDict[parentName] = childNameList
            weightDict[parentName] = 0 


    #######
    # realActCnt is the a3e parse result of activities 

    realActCnt = len(tmpVexList)

    print "realActCnt: " + str(realActCnt)

    cmd = '''echo "the number of Activities" {0} "parsing by a3e" >> {1}'''.format(realActCnt,outputPath)
    os.system(cmd)
    
    # MainActivity always should be parent if not sth. wrong(a3e parse wrong)
    # if all the vexs do not include the MainActivity sth. wrong 
    if not MainActivity in parentActNameCollection:
        print "The MainActivity not in the  parentActNameCollection"
        findflag=0

    if not MainActivity in tmpVexList:
        print "The a3e do not parse the MainActivity, the satg do not include the MainActivity"
        findflag = 0

    print "after judging the real findflag: " + str(findflag)
    graphCnt = len(edgeDict)
    
    # 0CB83F1C2EC5E43D
    if findflag==1:
        weightDict[MainActivity]=9999

    for key in parentActNameCollection:         # MainActivity -> LeaderboarderExporer

        for keyB in parentActNameCollection:    # LeaderboarderExporer -> ScoreExplorer ScoreExplorer-> ScorePoster

            if key != keyB:

                childNameList = edgeDict[key]   

                if keyB in childNameList:
                    weightDict[key] = weightDict[key] + weightDict[keyB] + 2
                    weightDict[keyB] += 1
                    graphCnt = graphCnt - 1

    
    sortWeight = sorted(weightDict.items(), key=lambda x:x[1],reverse=True)
    print sortWeight

    # we should consider this situation 
    # 4-> 2,1 (1)
    # 2-> 3,1 (1)
    # 3-> 6,7 (0)

        

    for key in parentActNameCollection:

        for keyB in parentActNameCollection:

            if (key != keyB) and (weightDict[key] !=0) and (weightDict[key]==weightDict[keyB]):

#                print "weightDict[keyB]" + str(weightDict[key])

                childNameList = edgeDict[key]

                if keyB in childNameList:
                    weightDict[key] = weightDict[key] + weightDict[keyB] + 2
                    weightDict[keyB] += 1
                else:
                    childListACnt = len(edgeDict[key])
                    childListBCnt = len(edgeDict[keyB])
                    
                    e = sortWeight[0][0]
                    if childListACnt >= childListBCnt:
                        weightDict[key]  += childListACnt
                        if weightDict[e] <= weightDict[key] and (e!=key):
                            weightDict[e] += childListACnt
                    else:
                        weightDict[keyB] += childListBCnt
                        if weightDict[e] <= weightDict[keyB] and (e!=keyB):
                            weightDict[e] += childListBCnt


    sortWeight = sorted(weightDict.items(), key =lambda x:x[1],reverse=True)

    print sortWeight
    
    cmd = "echo {0} >> {1}".format(sortWeight,outputPath)
    os.system(cmd)
    

    parentActNameCollection = []

    for e in sortWeight:
        parentName = e[0]

        if not parentName in parentActNameCollection:
            parentActNameCollection.append(parentName)
    
    tmpParentNameList = parentActNameCollection


    eachapkSatgName = apkSatgPath.split("/")[-1].split(".")[0]

    
    splitParent = []
    splitEdgeCollection = []

    for i in range(len(edgeDict)):

        for parentName in tmpParentNameList:

            if not parentName in EdgeCollection:  # firstly, we add the highest weight value into the EdgeCollection
                EdgeCollection.append(parentName) # so we set a high value for the MainActivity  add [MA] and then add children
                splitParent.append(parentName)    # [MA] [LeaderboarderExporer][AE][UserExplorer][TimerExplorer][CE][GameFeed]
                splitEdgeCollection.append(parentName)

#                print "EdgeCollection: "
 #               print EdgeCollection
#
#                tips = "splitParent:".format(splitParent)
  #              print tips
 #               print splitParent
#                print parentName



                childActList = edgeDict[parentName]

                for child in childActList:
                    if not child in EdgeCollection:
                        EdgeCollection.append(child)
                        splitEdgeCollection.append(child) # add children ####### add parent and children in to the EdgeCollection

                #del sortWeight[parentName]
                tmpParentNameList.remove(parentName) # del [MA]
                
                # when we finish the up process
                # we add this situation into the EdgeCollection
                # 0->1,2,3,4,5
                # 2->6,7

                for child in childActList:  # [MA] {[LA],[AE],[UE],[TE],[CE],[GF]} so now we consider {...}
                    if child in tmpParentNameList: # someparents [LA] -> SE [CE]->[CI] child has in EdgeCollection, 
                        parentName = child         # and splitEdgeCollection

                        if parentName not in splitParent:
                            splitParent.append(parentName)
                            tmpParentNameList.remove(parentName) 

   #                     print "child in tmpParentNameList"
                        
  #                      print "parentName"
 #                       print parentName

 #                       print "tmpParentNameList"
#                        print tmpParentNameList
                        childActList = edgeDict[parentName]  # like [LA] -> SE, SP 

                        if parentName not in EdgeCollection:
                            EdgeCollection.append(parentName)
                            splitEdgeCollection.append(parentName)

                        for child in childActList:
                            if not child in EdgeCollection: # add [SE]
                            #    print "child not in EdgeCollection"
                                
                            #    print "child" + child
                            
                                EdgeCollection.append(child)
                                splitEdgeCollection.append(child)
                                
                             #   print "EdgeCollection"
                            #    print EdgeCollection

                        #del sortWeight[parentName]
                     #   tmpParentNameList.remove(parentName) 

                    # situation:
                    # 4->2,1
                    # 2->3

                # for some vex the parent has in the graph while their children still not in the EdgeCollection
                '''
                print "****************tmpParentNameList"
                print tmpParentNameList


                print "****************"
                print "**************88"

                print EdgeCollection
                '''

                for parentName in tmpParentNameList:  # consider: 0->1,2,3  1->5,  5->7 7->8 8->9

                    if parentName in EdgeCollection:  # like deep traverse  if parent in graph add all his children in the graph

            #            print "we are in parentName in EdgeCollection but children are not in there "
             #           print parentName
                        
                        if not parentName in splitParent:  
                            print "parentName: " + parentName
                            splitParent.append(parentName)
                            tmpParentNameList.remove(parentName)

                        childActList = edgeDict[parentName]

                    
                        for child in childActList:
                            if not child in EdgeCollection:
                                EdgeCollection.append(child)
                                splitEdgeCollection.append(child)
                                
                
                #for some children in the EdgeCollection but their parent not in the graph 
                # situation:
                # we have added 6->7 into the EdgeCollection
                # we should add 8->7
                # 9->7,10 into the EdgeCollection

                for j in range(len(sortWeight)):

                    for parentName in tmpParentNameList:   

                        childActList = edgeDict[parentName]

                        for child in childActList:
                            if child in EdgeCollection:

                                if not parentName in EdgeCollection:
                                    EdgeCollection.append(parentName)
                                    splitEdgeCollection.append(parentName)
                                    tmpParentNameList.remove(parentName)
                                    splitParent.append(parentName)

                                    for child in childActList:
                                    
                                        if child not in EdgeCollection:
                                            EdgeCollection.append(child)
                                            splitEdgeCollection.append(child)
                                    
                                    break 

                    if len(tmpParentNameList)==0:
                        break

                # children and parents have already in the EdgeCollection but splitParent not add the relationship
                
                tmpPCnt = len(tmpParentNameList)
                for k in range(tmpPCnt):

                    for parentName in tmpParentNameList:

                        if parentName in EdgeCollection:

                            if not parentName in splitParent:
                                splitParent.append(parentName)
                                tmpParentNameList.remove(parentName)  # splitParent add the tmpParentNameList should delete
                            
                            childActList = edgeDict[parentName]

                            for child in childActList:

                                if not child in EdgeCollection:
                                    EdgeCollection.append(child)
                                    splitEdgeCollection.append(child)  
                
        
                    if len(tmpParentNameList) == 0:
                        break 
                
                # if child in EdgeCollection but parent not in EdgeCollection

                break

        print eachapkSatgName


        eachAPKSatgPath = os.path.join(graphPath,eachapkSatgName)

        print i
        cmd = '''echo "t"{0} >>{1}'''.format(i,eachAPKSatgPath)
        os.system(cmd)

        

        for key in splitParent:
            tmpList = edgeDict[key]

            for child in tmpList:
                sourceName = key 
                targetName = child 

#                source = splitEdgeCollection.index(sourceName)
#                target = splitEdgeCollection.index(targetName)

                source = EdgeCollection.index(sourceName)
                target = EdgeCollection.index(targetName)

                print "e " + sourceName + " --> " + targetName
                print "e " + str(source) + " --> " + str(target)
#                print "e " + str(sourceALL) + " --> " + str(targetALL)
                
                
                cmd = "echo {0} {1} >> {2}".format(source,target,eachAPKSatgPath)
                os.system(cmd)
            
                try:
                    cmd1 = '''echo "e " {0} " --> " {1} >> {2}'''.format(sourceName,targetName,outputPath)
                    os.system(cmd1)
                except:
                    cmd = "echo {0} {1} >> {2}".format(sourceName.encode('utf-8'),targetName.encode('utf-8'),eachAPKSatgPath)
                    os.system(cmd1)

#                cmd2 = '''echo "e " {0} " --> " {1} >> {2}'''.format(source,target,outputPath)
 #               os.system(cmd2)

    
                cmd3 = '''echo "e " {0} " --> " {1} >> {2}'''.format(source,target,outputPath)
                os.system(cmd3)


        splitParent = []
        splitEdgeCollection = []


        if len(tmpParentNameList)==0:
            break 



if __name__ == '__main__':

    APKList = os.listdir(APKPath)

    for apk in APKList:
        eachAPKPath = os.path.join(APKPath,apk)

        manifestPath = os.path.join(eachAPKPath,"AndroidManifest.xml")

        apk_satgFile = apk + ".apk.g.xml"

        apkSatgPath = os.path.join(satgPath,apk_satgFile)

        print "******************"

        if not os.path.exists(manifestPath):
            tips = "we cannot find the AndroidManifest.xml file of {0} ".format(apk)
            print tips 
            continue

        if not os.path.exists(apkSatgPath): # sometimes the a3e may cannot parse the satg file (without the AndroidManifest.xml)
            tips = "we cannot find the satg file of {0}".format(apkSatgPath) # is not frequent than without the satg file 
            print tips 
            continue 
        
        # invoke the function 

        exitsPathDet = os.path.join(graphPath,apk)
        if os.path.exists(exitsPathDet):
            print "The file {0} exists.".format(apk)


        getTheEdgeSet(manifestPath,apkSatgPath)



print "all work is done!"
