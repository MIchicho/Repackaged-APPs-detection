#!/usr/bin/env python
# coding=utf-8
'''
@ author   : chicho
@ data     : 2015-03-03
@ function : get the statis ferature of APK and insert into the databases
             1. parse AndroidManifest.xml file
             2. parse res file 
             3. insert into database 
@ running  : python calculate_resref.py
@ note     : we need touch a file --> /home/chicho/Workspace/ResDroid/staout.txt 
'''

import os
import sys 
import conf
import MySQLdb
try:
    import xml.etree.cElementTree as ET 
except ImportError:
    import xml.etree.ElementTree as ET
from xml.dom import minidom


print'''
================================================
You can use the default apk files's path or input the path you like!
usage: python findnoProcess.py <apk_path> <forgator_path>
Example : python calculate_resref.py /home/chicho/result/APK_1_ARCADE /home/chicho/result/sootAndroidOut_1_ARCAD
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
    path = "/home/chicho/result/APK_2_DEMO"
    guiPath = "/home/chicho/result/sootAndroidOut_2_DEMO"
else:
    path = raw_input("you APK path:\n")
    #judge you input apk_path right
    if not os.path.exists(path):
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)
    
    
    guiPath = raw_input("Inpur the path processed by Gator: \n")
    if not os.path.exists(guiPath): 
        print "Cannot find the path, please check you input path!:p\n"
        sys.exit(1)



statoutPath = "/home/chicho/Workspace/ResDroid/staout.txt"



#*********************************
#
#----------------------------
# Database connection
#----------------------------
#


def connect_db():
    con = MySQLdb.connect(
        host = conf.DB_HOST,
        user = conf.DB_USER,
        passwd = conf.DB_PASSWD,
        db = conf.DB_NAME,
        charset = 'utf8')


    return con 

conn = connect_db()
curs = conn.cursor()




#*********************************


def get_Category():

    category = "other"

    plist = guiPath.split("/")

    cateName = plist.pop()


    if cateName == "sootAndroidOut_1_ARC":
        category = "1_ARCADE"

    elif cateName == "sootAndroidOut_2_DEMO":
        category = "2_DEMO"
        
    elif cateName == "sootAndroidOut_3_ENT":
        category = "3_ENTERTANMENT"

    elif cateName == "sootAndroidOut_4_FIN":
        category = "4_FINANCE"

    elif cateName == "sootAndroidOut_5_HEA":
        category == "5_HEALTH"

    elif cateName == "sootAndroidOut_6_LIB":
        category = "6_LIBRARIES"

    elif cateName == "sootAndroidOut_7_LIF":
        category = "7_LIFESTYLE"

    elif cateName == "sootAndroidOut_8_MUL":
        category = "8_MULTIMEDIA"

    elif cateName == "sootAndroidOut_9_NEWS":
        category = "9_NEWS"

    elif cateName == "sootAndroidOut_10_REF":
        category = "10_REFERENCE"

    elif cateName == "sootAndroidOut_11_THE":
        category = "11_THEMES"

    elif cateName == "sootAndroidOut_12_TRA":
        category = "12_TRAVEL"

    elif cateName == "sootAndroidOut_13_BRA":
        category = "13_BRAIN"

    elif cateName == "sootAndroidOut_14_CARDS":
        category = "14_CARDS"

    elif cateName == "sootAndroidOut_15_CAS":
        category = "15_CASUAL"

    elif cateName == "sootAndroidOut_16_COMICS":
        category = "16_COMICS"

    elif cateName == "sootAndroidOut_17_COMM":
        category = "17_COMMUNICATION"

    elif cateName == "sootAndroidOut_18_PRO":
        category = "18_PRODUCTIVITY"

    elif cateName == "sootAndroidOut_19_SHOP":
        category = "19_SHOPPING"

    elif cateName == "sootAndroidOut_20_SOC":
        category = "20_SOCIAL"

    elif cateName == "sootAndroidOut_21_SPO":
        category = "21_SPORTS"

    elif cateName == "sootAndroidOut_22_TOOLS":
        category = "22_TOOLS"

    elif cateName == "sootAndroidOut_23_BUS":
        category = "23_BUSINESS"

    elif cateName == "sootAndroidOut_24_PER":
        category = "24_PERSONALIZATION"

    elif cateName == "sootAndroidOut_25_WALL":
        category = "25_APP_WALLPAPER"

    elif cateName == "sootAndroidOut_26_SPORT":
        category = "26_SPORTS_GAME"

    elif cateName == "sootAndroidOut_27_GAME":
        category = "27_GAMW_WALLPAPER"
    
    elif cateName == "sootAndroidOut_28_RAC":
        category = "28_RACING"

    elif cateName == "sootAndroidOut_29_GAME":
        category = "29_GAME_WIDGETS"

    elif cateName == "sootAndroidOut_30_WID":
        category = "30_APP_WIDGETS"

    elif cateName == "sootAndroidOut_31_EDU":
        category = "31_EDUCATION"

    elif cateName == "sootAndroidOut_32_MED":
        category = "32_MEDICAL"

    elif cateName == "sootAndroidOut_33_MUS":
        category = "33_MUSIC"

    elif cateName == "sootAndroidOut_34_PHO":
        category = "34_PHOTOGRAPHY"

    elif cateName == "sootAndroidOut_35_TRANS":
        category = "35_TRANSPORTATION"

    elif cateName == "sootAndroidOut_36_WEATHER":
        category = "36_WEATHER"

    elif cateName == "origapps":
        category = "gt_original"

    elif cateName == "repackaged":
        category = "gt_repackaged"

    else:
        category = "other"

    return category


#*********************************




def count_ref(apkPath,apkname):
    resPath = os.path.join(apkPath,"res")
    
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
                if not pngfile.endswith(".png"):
                    all_png -= 1

        
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
                            missLogPath = "/home/chicho/Workspace/ResDroid/missLog/" 
                            cmd = "cp -r {0} {1}".format(apkPath,missLogPath)
                            os.system(cmd)
                            cmd1 = "echo {0}, {1} cannot be parsed!>> output.txt".format(apkPath,xmlfilePath)
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


                        if xmlfile == "dimens.xml":
                            dimen_list = xmldoc.getElementsByTagName('dimen')
                            dimen_cnt = len(dimen_list)


                        if xmlfile == "styles.xml":
                            style_list = xmldoc.getElementsByTagName('style')
                            style_cnt = len(style_list)

                        if xmlfile == "attrs.xml":
                            nodes = xmldoc.getElementsByTagName('attr')
                            for n in nodes:
                                if n.getAttribute("format") == "integer":
                                    integer_cnt += 1
                    
                    else:
                        cmd = "echo {0}, doesn't exists >> output.txt".format(apkPath)
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
        avg_xml = all_xml/resfile_cnt

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
        cmd = "echo {0},cannot find AndroidManifest.xml >> output.txt".format(apkPath)
        return


    category = get_Category()


    sql_tmp = 'INSERT INTO `statis_feature` (\
            app_name, app_path, category, activity_cnt, perm_cnt, if_cnt, png_cnt,\
            xml_cnt, id_cnt, drawable_cnt, string_cnt, color_cnt, style_cnt,\
            dimen_cnt, layout_cnt, xml_ref, integer_cnt, array_cnt, service_cnt, receiver_cnt) \
            VALUES("{0}", "{1}", "{2}", {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18},{19})'
    

    sql = sql_tmp.format(apkname, apkPath, category,activity_cnt, perm_cnt, if_cnt, avg_png, avg_xml, id_cnt, drawable_cnt, \
                         string_cnt, color_cnt, style_cnt, dimen_cnt, layout_cnt, ref_xml, integer_cnt, array_cnt, service_cnt, receiver_cnt)

    
    try:
        curs.execute(sql)
        conn.commit()

        tips = "now insert {0} into statis_feature table".format(apkPath)
        print tips

        cmd = "echo {0} >> staout.txt".format(apkPath)
        os.system(cmd)
    except:
        cmd = "echo {0} >> output.txt".format(apkPath)
        os.system(cmd)

    
    cmd = "echo {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16} >> statis_feature.txt".format(\
                activity_cnt, perm_cnt, if_cnt, avg_png, avg_xml, id_cnt, drawable_cnt, string_cnt, color_cnt,\
                style_cnt, dimen_cnt, layout_cnt, ref_xml,integer_cnt,array_cnt,service_cnt,receiver_cnt)
    os.system(cmd)


    '''
    print "act_cnt:",activity_cnt,"perm_cnt",perm_cnt,"intent-filter",if_cnt,"png",avg_png,"avg_xml",avg_xml,"service_cnt",service_cnt,"receiver_cnt",receiver_cnt
    print "id",id_cnt,"drawable",drawable_cnt,"string",string_cnt,"color",color_cnt,"style",style_cnt,"dimen",dimen_cnt,"layout",layout_cnt,"xml",ref_xml,"integer",integer_cnt,"array",array_cnt
    '''




if __name__ == "__main__":
    
    apkList = os.listdir(path)

    guiList = os.listdir(guiPath)
    
    f = open(statoutPath,'r')
    processedApkList = []
    for apk in f.readlines():
        apk = apk.replace("\n","")
        processedApkList.append(apk)


    for APK in apkList:
        apkPath = os.path.join(path,APK)
            
        if apkPath in processedApkList:
            tips = "{0} has already exists!".format(apkPath)
            print tips
            continue


        if os.path.exists(apkPath):
            for guifile in guiList:
                if guifile.endswith(".xml"):
                    guiname = guifile.split("-") 
                    guiname.pop()

                    guiname = '-'.join(guiname)

                    if guiname == APK:
                        count_ref(apkPath,APK)


    curs.close()
    conn.close()


print "all work done!"

