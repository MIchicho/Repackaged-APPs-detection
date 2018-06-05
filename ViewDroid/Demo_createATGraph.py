#!/usr/bin/env python
# coding=utf-8
import os
import sys
import xml.dom.minidom
import operator


APKPath = "/home/chicho/test/problem_Test/apk/"

satgPath = "/home/chicho/test/problem_Test/satg/"


def findMainActivity(manifestPath):
    
    print "we are in findMainActivity"

    findflag = 0
    MainActivity = ""
    actCnt=0
    package=""

    if not os.path.exists(manifestPath): 
        return (findflag,MainActivity,package)
   
    
    try:
        dom = xml.dom.minidom.parse(manifestPath)
    except: 
        return (findflag,MainActivity,package)

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


    
    return (findflag,MainActivity,package)


#
#*************************************
# get all the nodes and the Edge 
# parse the satg
# Create the ATG
#*************************************



def getTheEdgeSet(manifestPath,apkSatgPath):

    print "We are in the getTheEdgeSet"

    findflag,MainActivity,package = findMainActivity(manifestPath)
    
    print "*********************"

    print "findflag:"
    print findflag
    print MainActivity
    print package 

    EdgeCollection=[]
    edgeDict={}
    parentActNameCollection=[]

    if not os.path.exists(apkSatgPath):
        print "The satg file not exists."
        return (EdgeCollection,edgeDict,parentActNameCollection)


    ##################

    try:
        dom = xml.dom.minidom.parse(apkSatgPath)
    except:
        return (EdgeCollection,edgeDict,parentActNameCollection)

    root = dom.documentElement

    parentActList = root.getElementsByTagName('Activity')

    weightDict={}

    tmpVexList = []

    for activity in parentActList:
        parentName = activity.getAttribute('name')

        if parentName.startswith('com.google.ads'):
            continue 

        if parentName.startswith('com.admob.android'):
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

    
    if not MainActivity in parentActNameCollection:
        findflag=0

    if not MainActivity in tmpVexList:
        findflag = 0


    graphCnt = len(edgeDict)

    if findflag==1:
        weightDict[MainActivity]=9999

    for key in parentActNameCollection:

        for keyB in parentActNameCollection:

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

                    if childListACnt >= childListBCnt:
                        weightDict[key]  += childListACnt
                    else:
                        weightDict[keyB] += childListBCnt 


    sortWeight = sorted(weightDict.items(), key =lambda x:x[1],reverse=True)

    print sortWeight

    

    parentActNameCollection = []

    for e in sortWeight:
        parentName = e[0]

        if not parentName in parentActNameCollection:
            parentActNameCollection.append(parentName)
    
    tmpParentNameList = parentActNameCollection


    eachapkSatgName = apkSatgPath.split("/")[-1].split(".")[0]

    
    splitParent = []
    for i in range(len(edgeDict)):

        for parentName in tmpParentNameList:

            if not parentName in EdgeCollection:
                EdgeCollection.append(parentName)
                splitParent.append(parentName)

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

                #del sortWeight[parentName]
                tmpParentNameList.remove(parentName)
                
                # when we finish the up process
                # we add this situation into the EdgeCollection
                # 0->1,2,3,4,5
                # 2->6,7

                for child in childActList:
                    if child in tmpParentNameList:
                        parentName = child

                        if parentName not in splitParent:
                            splitParent.append(parentName)
                            tmpParentNameList.remove(parentName) 

   #                     print "child in tmpParentNameList"
                        
  #                      print "parentName"
 #                       print parentName

 #                       print "tmpParentNameList"
#                        print tmpParentNameList
                        childActList = edgeDict[parentName]

                        if parentName not in EdgeCollection:
                            EdgeCollection.append(parentName)

                        for child in childActList:
                            if not child in EdgeCollection:
                            #    print "child not in EdgeCollection"
                                
                            #    print "child" + child
                            
                                EdgeCollection.append(child)
                                
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

                    if parentName in EdgeCollection:

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
                                
                
                #for some children in the EdgeCollection but their parent not in the graph 
                # situation:
                # we have added 6->7 into the EdgeCollection
                # we should add 8->7
                # 9->7,10 into the EdgeCollection

                for parentName in tmpParentNameList:

                    childActList = edgeDict[parentName]

                    for child in childActList:
                        if child in EdgeCollection:

                            if not parentName in EdgeCollection:
                                EdgeCollection.append(parentName)
                                tmpParentNameList.remove(parentName)
                                splitParent.append(parentName)

                                for child in childActList:
                                    
                                    if child not in EdgeCollection:
                                        EdgeCollection.append(child)

                                break 

                break

        print eachapkSatgName


        print i
        cmd = '''echo "t"{0} >>{1}'''.format(i,eachapkSatgName)
        os.system(cmd)

        for key in splitParent:
            tmpList = edgeDict[key]

            for child in tmpList:
                sourceName = key 
                targetName = child 

                source = EdgeCollection.index(sourceName)
                target = EdgeCollection.index(targetName)

                print "e " + sourceName + " --> " + targetName
                print "e " + str(source) + " --> " + str(target)

                cmd = "echo {0} {1} >> {2}".format(source,target,eachapkSatgName)
                os.system(cmd)



        splitParent = []


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

        getTheEdgeSet(manifestPath,apkSatgPath)

    
