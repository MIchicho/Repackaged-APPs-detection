#!/usr/bin/env python
# coding=utf-8
'''
@ author   : chicho
@ data     : 2015-03-12
@ running  : python createSPcluster.py
@ function : this file is create the data file for sp-cluster 

sp need data :
each app :
0:123 1:2 3:34 4:5 ... 16:232
'''


import os
import MySQLdb
import conf

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

if __name__ == '__main__':
    sql = "select  activity_cnt, perm_cnt, if_cnt, png_cnt, xml_cnt, id_cnt,\
    drawable_cnt, string_cnt, color_cnt, style_cnt,dimen_cnt,layout_cnt,xml_ref,integer_cnt,\
    array_cnt,service_cnt, receiver_cnt from statis_feature"

    curs.execute(sql)

    res = curs.fetchall()

    for row in res:
        cmd = "echo 0:{0} 1:{1} 2:{2} 3:{3} 4:{4} 5:{5} 6:{6} 7:{7} 8:{8} 9:{9} 10:{10} 11:{11} 12:{12} 13:{13} 14:{14} 15:{15} 16:{16}>>spdata.txt".\
		format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
        os.system(cmd)
      
    curs.close()
    conn.close()
   

   


print "all work done!"
