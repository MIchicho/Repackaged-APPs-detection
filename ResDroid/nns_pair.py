#!/usr/bin/env python
# coding=utf-8
import os
import MySQLdb
import conf 

#-------------------------------
# Database connection
#-------------------------------

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

# bug info
missPath = "/home/chicho/Workspace/ResDroid/missLog/"
missAPKLog = os.path.join(missPath, "missLog.txt")
missgatorLog = os.path.join(missPath, "missGatorLog.txt")




# cat_APK="APK_1_ARCADE" 
#cat_gator="sootAndroidOut_1_ARCADE"
#-----------------------------------------------------
def get_apkGui_name(apk_path,cat_APK,cat_gator):
    gator_apk = []   # for_gator_apkPath, gator_apk_path
    path = "/home/chicho/result/"
    apkname = os.path.basename(apk_path)
    
    cat_APKPath = os.path.join(path,cat_APK)
    apkFileList = os.listdir(cat_APKPath)

    gator_apk_path = os.path.join(path.cat_gator)
    gatoredAPKList = os.listdir(gator_apk_path)

    if apkname.endswith(".apk"):
        portion = os.path.splitext(apkname)
        APK = portion[0]
        
        if APK in apkFileList:
            for_gator_apkPath = os.path.join(cat_APKPath,APK)  # for_gator_apkPath

            for guifile in gatoredAPKList:
                guixml = guifile.splite("-")[-2]
                if ( APK == guixml ):
                    gator_path = os.path.join(gator_apk_path,guifile) #gator_path
                else:
                    gator_path =""
                    cmd = "echo {0},{1} >> {2}".format(APK,missgatorLog)
                    os.system(cmd)
        else:
            for_gator_apkPath = ""
            cmd = "echo {0} >> {1}".format(APK, missAPKLog)
            os.system(cmd)

    gator_apk.append(for_gator_apkPath)
    gator_apk.append(gator_path)


    return gator_apk  



# get each cluster info about guiHierarchy to calculat the diff(GuiSeq,EventSeq)
# we should send the parameter apk process by apktool and dex2jar dir==>"APKDEMO"
# and the outPut processed by gator 
def find_path(apk_path,category):
    gator_apk =[]
    if (category == "1_ARCADE"):
        gator_apk = get_apkGui_name(apk_path,"APK_1_ARCADE","sootAndroidOut_1_ARC")


    elif (category == "2_DEMO"):
        gator_apk = get_apkGui_name(apk_path,"APKDEMO","sootAndroidOut_2_DEMO")

    elif (category == "3_ENTERTAINMENT"):
        gator_apk = get_apkGui_name(apk_path,"APKENTETAINMENT","sootAndroidOutAPK_3_ENT")

    elif (category == "4_FINANCE"):
        gator_apk = get_apkGui_name(apk_path,"APK_4_FINANCE","sootAndroidOut_4_FIN")

    elif (category == "5_HEALTH"):
        gator_apk = get_apkGui_name(apk_path,"APK_5_HEALTH","sootAndroidOut_5_HEA")

    elif (category == "6_LIBRARIES"):
        gator_apk = get_apkGui_name(apk_path,"APK_6_LIBRARIES","sootAndroidOut_6_LIB")

    elif (category == "7_LIFESTYLE"):
        gator_apk = get_apkGui_name(apk_path,"APK_7_LIFESTYLE","sootAndroidOut_7_LIFESTYLE")

    elif (category == "8_MULTIMEDIA"):
        gator_apk = get_apkGui_name(apk_path,"APK_8_MULTIMEDIA","sootAndroidOut_8_MUL")

    elif (category == "9_NEWS"):
        gator_apk = get_apkGui_name(apk_path,"APK_9_NEWS","sootAndroidOut_9_NEWS")

    elif (category == "10_REFERENCE"):
        gator_apk = get_apkGui_name(apk_path,"APK_10_REF","sootAndroidOut_10_REF")

    elif (category == "11_THEMES"):
        gator_apk = get_apkGui_name(apk_path, "APK_11_THEME","sootAndroidOut_11_THE")

    elif (category == "12_TRAVEL"):
        gator_apk = get_apkGui_name(apk_path, "APK_12_TRA","sootAndroidOut_12_TRA")

    elif (category == "13_BRAIN"):
        gator_apk = get_apkGui_name(apk_path, "APK_13_BRAIN","sootAndroidOut_13_BRAIN")

    elif (category == "14_CARDS"):
        gator_apk = get_apkGui_name(apk_path,"APK_14_CARDS","sootAndroidOut_14_CARDS")

    elif (category == "15_CASUAL"):
        gator_apk = get_apkGui_name(apk_path,"APK_15_CASUAL","sootAndroidOut_15_CAS")

    elif (category == "16_COMICS"):
        gator_apk = get_apkGui_name(apk_path,"APK_16_COMICS","sootAndroidOut_16_COM")

    elif (category == "17_COMMUNICATION"):
        gator_apk = get_apkGui_name(apk_path,"APK_17_COMMUNICATION","sootAndroidOut_17_COMM")

    elif (category == "18_PRODUCTIVITY"):
        gator_apk = get_apkGui_name(apk_path,"APK_18_PROD","sootAndroidOut_18_PROD")

    elif (category == "19_SHOPPING"):
        gator_apk = get_apkGui_name(apk_path,"APK_19_SHOP","sootAndroidOut_19_SHOP")

    elif (category == "20_SOCIAL"):
        gator_apk = get_apkGui_name(apk_path,"APK_20_SOCIAL","sootAndroidOut_20_SOC")

    elif (category == "21_SPORTS"):
        gator_apk = get_apkGui_name(apk_path,"APK_21_SPORTS","sootAndroidOut_21_SPORTS")

    elif (category == "22_TOOLS"):
        gator_apk = get_apkGui_name(apk_path,"APK_22_TOOLS","sootAndroidOut_22_TOOLS") 

    elif (category == "23_BUSINESS"):
        gator_apk = get_apkGui_name(apk_path,"APK_23_BUS","sootAndroidOut_23_BUS")

    elif (category == "24_PERSONNALIZATION"):
        gator_apk = get_apkGui_name(apk_path, "APK_24_PER","sootAndroidOut_24_PER")

    elif (category == "25_APP_WALLPAPER"):
        gator_apk = get_apkGui_name(apk_path,"APK_25_APP","sootAndroidOut_25_APP")

    elif (category == "26_SPORTS_GAMES"):
        gator_apk = get_apkGui_name(apk_path,"APK_26_GAME","sootAndroidOut_26_GAMES")

    elif (category == "27_GAME_WALLPAPER"):
        gator_apk = get_apkGui_name(apk_path,"APK_27_WALL","sootAndroidOut_27_WALL") 

    elif (category == "28_RACING"):
        gator_apk = get_apkGui_name(apk_path,"APK_28_PAC","sootAndroidOut_28_RAC") 

    elif (category == "29_GAME_WIDGETS"):
        gator_apk = get_apkGui_name(apk_path,"APK_29_WIDG","sootAndroidOut_29_WIDG")

    elif (category == "30_APP_WIDGETS"):
        gator_apk = get_apkGui_name(apk_path,"APK_30_APP","sootAndroidOut_30_APP")

    elif (category == "31_EDUCATION"):
        gator_apk = get_apkGui_name(apk_path,"APK_31_EDU","sootAndroidOut_31_EDU")

    elif (category == "32_MEDICAL"):
        gator_apk = get_apkGui_name(apk_path,"APK_32_MED","sootAndroidOut_32_MED")

    elif (category == "33_MUSIC_AND_AUDIO"):
        gator_apk = get_apkGui_name(apk_path,"APK_33_MUS","sootAndroidOut_33_MUS")

    elif (category == "34_PHOTOGRAPHY"):
        gator_apk = get_apkGui_name(apk_path,"APK_34_PHO","sootAndroidOut_34_PHO")

    elif (category == "35_TRANSPOPRTATION"):
        gator_apk = get_apkGui_name(apk_path,"APK_35_TRANS","sootAndroidOut_35_TRAN") 

    elif (category == "36_WEATHER"):
        gator_apk = get_apkGui_name(apk_path,"APK_36_WEATHER","sootAndroidOut_36_WEATHER")
    else:
        return gator_apk 
    
    return gator_apk



def select_nns_pair():
    sql ='''select app_id,nns_cid,category,apk_path from all_apps,stat_feature 
        where stat_feature.app_id=all_apps.id and category is NOT NULL'''
        #and category is NOT \"original\" and category is NOT \"repackaged\"''' 
        
    
    curs.execute(sql)

    res = curs.fetchall()

    for row in res:
        app_id = row[0]
        nns_cid = row[1]
        category = row[2]
        apk_path = row[3]

        sql_tmp = '''INSERT INTO google_nns(app_id,nns_cid,category,apk_path)VALUES({0},{1},'{2}','{3}')'''
    
        sql = sql_tmp.format(app_id,nns_cid,category,apk_path)
        curs.execute(sql)
    
        conn.commit()

        apkname = os.path.basename(apk_path)

        cmd = "now it insert {0}".format(apkname)

        print cmd 

def select_cls_app():
    sql = '''select app_id, nns_cid, cluster_id, category, apk_path 
        from all_apps,stat_feature 
        where stat_feature.app_id=all_apps.id and 
        cluster_id=1 and category is NOT NULL and category is NOT 'original' and category is NOT `repackaged`'''
    
    curs.execute(sql)

    res = curs.fetchall()

    for row in res:
        app_id = row[0]
        nns_cid = row[1]
        cluster_id = row[2]
        category = row[3]
        apk_path = row[4]
       
        gator_apk = find_path(apk_path,category)

        for_gator_apkPath = gator_apk[0]

        gator_path = gator_apk[1]
        sql_tmp ='''INSERT INTO nns_pair(app_id,nns_cid,cluster_id,
            category,apk_path,for_gator_apkPath,gator_path)
            VALUES ({0},{1},{2},'{3}','{4}','{5}','{6}')'''

        sql = sql_tmp.format(app_id,nns_cid,cluster_id,category,apk_path,for_gator_apkPath,gator_path)

        curs.execute(sql)

        conn.commit()





def get_process_apps():
    sql="select * from stat_feature"

    curs.execute(sql)
    
    processed_apps = curs.fetchall()

    return processed_apps




if __name__ == '__main__':


   # select_cls_app()
    

    select_nns_pair()

    curs.close()
    conn.close()





