#!/usr/bin/env python
# coding=utf-8
'''
@ author   : chicho
@ date     : 2015-03-12
@ running  : python  insertStatis_feature.py
@ function : this file is create a kdtree_need data all the needed data stores in the database
             stat_feature1
                1. get the data from the statis_feature
                2. insert the needed data into stat_feature1   
                3. the KD-tree need data like appid : f1 f2 f3 f4 f5...
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
    array_cnt,service_cnt, receiver_cnt,app_name from statis_feature"

    curs.execute(sql)

    res = curs.fetchall()

    for row in res:
        sql_tmp = 'INSERT INTO `stat_feature1` (\
        app_id, activity_cnt, perm_cnt, if_cnt, png_cnt,xml_cnt,id_cnt,drawable_cnt, ref_string,ref_color,\
        ref_style, ref_dimen, ref_layout, ref_xml, ref_integer,ref_array,service_cnt, receiver_cnt) \
        VALUES({0}, {1}, {2}, {3}, {4}, {5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17})'


        sql = sql_tmp.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17])
        

        curs.execute(sql)
        conn.commit()
        '''
        try:
            curs.execute(sql)
            conn.commit()
            cmd = "insert {0} into stat_feature1".format(row[18])
            print cmd 
        except:
            conn.rollback()
            print "something wrong!\n"
        '''
    curs.close()
    conn.close()
   

   


print "all work done!"
