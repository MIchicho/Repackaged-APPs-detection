#!/usr/bin/env python
# coding=utf-8
'''
@ author    : chicho
@ data      : 2015-03-12
@ running   : python createDBSCANdata.py
@ function  : this file is get the 17-dimen data from the statis_feature and create the arff file 
              to provide the dbscan algorithm
              1. select data from statis_feature
              2. 1,3,6,0 >> statis_feature.arff 
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
    sql = "select _id, activity_cnt, perm_cnt, if_cnt, png_cnt, xml_cnt, id_cnt,\
    drawable_cnt, string_cnt, color_cnt, style_cnt,dimen_cnt,layout_cnt,xml_ref,integer_cnt,\
    array_cnt,service_cnt, receiver_cnt from statis_feature"

    curs.execute(sql)

    res = curs.fetchall()

    for row in res:
        cmd = "echo {0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16} >> statis_feature.arff".\
                format(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17])
        os.system(cmd)



    curs.close()
    conn.close()
   

   


print "all work done!"
