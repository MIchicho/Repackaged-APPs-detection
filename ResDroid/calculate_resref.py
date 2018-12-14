#!/usr/bin/env python
# coding=utf-8
'''
@ author   : chicho
@ data     : 2017-08-11 
@ function : get the statis ferature of APK and insert into the databases
             1. parse AndroidManifest.xml file
             2. parse res file 
             
@ running  : python calculate_resref.py
@ note     : we need touch a file --> /home/chicho/Workspace/ResDroid/staout.txt 
'''

import os
import sys 
import time 


try:
    import xml.etree.cElementTree as ET 
except ImportError:
    import xml.etree.ElementTree as ET
from xml.dom import minidom


print'''
===================================================================
input : 0 -> original path 
input : 1 -> repackaged path 

===================================================================
'''

input = raw_input("your choice ? 0 or 1: \n")

while (input != '0') and (input != '1'):
    print "you input is wrong!"
    input = raw_input("your choice ? 0 or 1: \n")



if (input == '0'):
    apkPath = "/home/chicho/workspace/repackaged/result/original/"
    outputPath = "/home/chicho/workspace/repackaged/ResDroid/original.txt"

if (input == '1'):
    apkPath = "/home/chicho/workspace/repackaged/result/repackaged/"
    outputPath = "/home/chicho/workspace/repackaged/ResDroid/repackaged.txt"


statoutPath = "/home/chicho/workspace/repackaged/ResDroid/staout.txt"

#*********************************





def count_ref(apkPath,apkname):

    try:
        resPath = os.path.join(apkPath,"res")
    except:
        return 
    
    resfilelist = os.listdir(resPath)
    resfile_cnt = len(resfilelist)
    
    
    avg_png = 0 # 4
    avg_xml = 0 # 5
    id_cnt = 0
    drawable_cnt = 0
    string_cnt = 0
    color_cnt = 0
    style_cnt = 0
    dimen_cnt = 0
    layout_cnt = 0
    ref_xml = 0
    integer_cnt = 0
    array_cnt = 0


    dr_cnt = 0
    all_xml = 0
    all_png = 0
    val_cnt = 0
    attr_cnt = 0 

    for resfile in resfilelist:
        #************************
        # 5. calculate avg_xml 
        resfilePath = os.path.join(resPath,resfile)  # each apk res path 
        xmlList = os.listdir(resfilePath)

         

        all_xml += len(xmlList)
        for xmlfile in xmlList:
            if not xmlfile.endswith('.xml'):
                all_xml -= 1  


        #************************
        # 4. calculate avg_png 
        if resfile.startswith("drawable"):
            dr_cnt += 1
            drawablePath = os.path.join(resPath,resfile)
            pngList = os.listdir(drawablePath)

            all_png += len(pngList)

            for pngfile in pngList:
                if not pngfile.endswith(".png") :
                    all_png -= 1

        if resfile.startswith("values"):
            val_cnt +=1


        #***********************
        # calculate id string color style dimen integer array 
        if resfile == "values":
            valuesPath = os.path.join(resPath, resfile)
            valuelist = os.listdir(valuesPath)
            if len(valuelist) !=0:
                for xmlfile in valuelist:
                    xmlfilePath = os.path.join(valuesPath,xmlfile)


                    if os.path.exists(xmlfilePath):
                        try:
                            xmldoc = minidom.parse(xmlfilePath)
                        except:
			    tips = "{0} cannot be parsed!".format(xmlfilePath)
                            print tips
                            missLogPath = "/home/chicho/workspace/repackaged/ResDroid/missLog/" 
                            if not os.path.exists(missLogPath):
                                os.makedirs(missLogPath)
                            cmd = "cp -r {0} {1}".format(apkPath,missLogPath)
                            os.system(cmd)
                            cmd1 = "echo {0}, {1} cannot be parsed!>> LOG".format(apkPath,xmlfilePath)
                            os.system(cmd1)

                            return

                        
                        if xmlfile == "public.xml":
                            id_list = xmldoc.getElementsByTagName('public')
                            id_cnt = len(id_list)

                        if xmlfile == "arrays.xml":
                            array_list = xmldoc.getElementsByTagName('item')
                            array_cnt = len(array_list)


                        if xmlfile == "strings.xml":
                            string_list = xmldoc.getElementsByTagName('item')
                            string_cnt += len(string_list)
                            string_list1 = xmldoc.getElementsByTagName('string')
                            string_cnt += len(string_list1)


                        if xmlfile == "colors.xml":
                            color_list = xmldoc.getElementsByTagName('item')
                            color_cnt = len(color_list)

                        if xmlfile == "colors.xml":
                            color_list = xmldoc.getElementsByTagName('color')
                            color_cnt = len(color_list)+color_cnt

                        if xmlfile == "dimens.xml":
                            dimen_list = xmldoc.getElementsByTagName('dimen')
                            dimen_cnt = len(dimen_list)


                        if xmlfile == "styles.xml":
                            style_list = xmldoc.getElementsByTagName('style')
                            style_cnt = len(style_list)

                        if xmlfile == "attrs.xml":
                            nodes = xmldoc.getElementsByTagName('attr')
                            attr_cnt = len(nodes)

                            for n in nodes:
                                if n.getAttribute("format") == "integer":
                                    integer_cnt += 1
                    
                    else:
                        cmd = "echo {0}, doesn't exists >> LOG".format(apkPath)
                        os.system(cmd)
                        continue



        #***********************
        # calculate drawable
        if resfile == "drawable":
            drawablePath = os.path.join(resPath,"drawable")
            drawable_list = os.listdir(drawablePath)
            drawable_cnt = len(drawable_list)


        #**********************
        # calculate layout 
        if resfile == "layout":
            layoutPath = os.path.join(resPath,"layout")
            layout_list = os.listdir(layoutPath)
            layout_cnt = len(layout_list)

        #**********************
        # calculate xml 
        if resfile == "xml":
            xmlPath = os.path.join(resPath,"xml")
            xml_list = os.listdir(xmlPath)
            ref_xml = len(xml_list)

    
    
    if (resfile_cnt != 0):
        avg_xml = all_xml/(resfile_cnt - dr_cnt - val_cnt + 2)

    if (dr_cnt != 0):
        avg_png = all_png/dr_cnt 



#***********************************************

    manifestPath = os.path.join(apkPath,"AndroidManifest.xml")
    
    activity_cnt = 0
    perm_cnt = 0
    if_cnt = 0
    service_cnt = 0
    receiver_cnt = 0
    
    if os.path.exists(manifestPath):
        try:
            xmldoc = minidom.parse(manifestPath)
        except:
	    tips = "{0} cannot be parsed!".format(xmlfilePath)
	    print tips
            missLogPath = "/home/chicho/Workspace/ResDroid/missLog/"
            if not os.path.exists(missLogPath):
                os.makedirs(missLogPath)
            
            cmd = "cp -r {0} {1}".format(apkPath,missLogPath)
            os.system(cmd)
            cmd1 = "echo {1} cannot be parsed!>> output.txt".format(apkPath,xmlfilePath)
            os.system(cmd1)

            return                            


        permission_list = xmldoc.getElementsByTagName('uses-permission')
        perm_cnt = len(permission_list)

        activity_list = xmldoc.getElementsByTagName('activity')
        activity_cnt = len(activity_list)

        service_list = xmldoc.getElementsByTagName('service')
        service_cnt = len(service_list)

        if_list = xmldoc.getElementsByTagName('intent-filter')
        if_cnt = len(if_list)

        receiver_list = xmldoc.getElementsByTagName('receiver')
        receiver_cnt = len(receiver_list)
    else:
        cmd = "echo {0},cannot find AndroidManifest.xml >> LOG".format(apkPath)
        return


    

    '''
    sql_tmp = 'INSERT INTO `statis_feature` (\
            app_name, app_path, category, activity_cnt, perm_cnt, if_cnt, png_cnt,\
            xml_cnt, id_cnt, drawable_cnt, string_cnt, color_cnt, style_cnt,\
            dimen_cnt, layout_cnt, xml_ref, integer_cnt, array_cnt, service_cnt, receiver_cnt) \
            VALUES("{0}", "{1}", "{2}", {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18},{19})'
    

    sql = sql_tmp.format(apkname, apkPath,category,activity_cnt, perm_cnt, if_cnt, avg_png, avg_xml, id_cnt, drawable_cnt, \
                         string_cnt, color_cnt, style_cnt, dimen_cnt, layout_cnt, ref_xml, integer_cnt, array_cnt, service_cnt, receiver_cnt)

    
    exit
    '''
    '''
    cmd = "echo {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18}>>{19}".\
            format(apkname,activity_cnt,perm_cnt,if_cnt,avg_png,avg_xml,id_cnt,drawable_cnt,string_cnt,color_cnt,style_cnt,dimen_cnt,layout_cnt,ref_xml,integer_cnt,array_cnt,\
                  service_cnt,receiver_cnt,attr_cnt, outputPath)

    os.system(cmd)
   
    '''

    cmd = "echo {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11} >>{12}".\
            format(apkname,activity_cnt,perm_cnt,if_cnt,avg_png,avg_xml,id_cnt,drawable_cnt,string_cnt,layout_cnt,service_cnt,receiver_cnt,"Rep_coaseVec.csv")

    os.system(cmd)


    cmd = "echo {0},{1},{2},{3},{4},{5},{6},{7} >>{8}".\
            format(apkname,activity_cnt,perm_cnt,if_cnt,avg_png,avg_xml,id_cnt,string_cnt,"Rep_strictVector.csv")
    os.system(cmd)




    cmd = "echo {0} >> staout.txt".format(apkPath)
    os.system(cmd)
    
    print apkname

    
    '''
    cmd = "echo {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16} >> statis_feature.txt".format(\
                activity_cnt, perm_cnt, if_cnt, avg_png, avg_xml, id_cnt, drawable_cnt, string_cnt, color_cnt,\
                style_cnt, dimen_cnt, layout_cnt, ref_xml,integer_cnt,array_cnt,service_cnt,receiver_cnt)
    os.system(cmd)
    '''


    
    print "act_cnt:",activity_cnt,"perm_cnt",perm_cnt,"intent-filter",if_cnt,"png",avg_png,"avg_xml",avg_xml,"service_cnt",service_cnt,"receiver_cnt",receiver_cnt
    print "id",id_cnt,"drawable",drawable_cnt,"string",string_cnt,"color",color_cnt,"style",style_cnt,"dimen",dimen_cnt,"layout",layout_cnt,"xml",ref_xml,"integer",integer_cnt,"array",array_cnt,"attrs",attr_cnt





if __name__ == "__main__":
    
    start = time.time()
    apkList = os.listdir(apkPath)

#    guiList = os.listdir(guiPath)
    
    f = open(statoutPath,'r')
    processedApkList = []
    for apk in f.readlines():
        apk = apk.replace("\n","")
        processedApkList.append(apk)


    for APK in apkList:
        eachapkPath = os.path.join(apkPath,APK)
            
        if eachapkPath in processedApkList:
            tips = "{0} has already exists!".format(eachapkPath)
            print tips
            continue

        count_ref(eachapkPath,APK)
        


    f.close()
    end = time.time()

    elapse = end - start 

    print elapse

print "all work done!"

