#!/usr/bin/env python
# coding=utf-8
from __future__ import division 
import MySQLdb
import conf 


#
#-------------------------
# Database connection
#-------------------------
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


# we can get the gt pair by their name since they ori and rpck have the same name 
# we just get the name from the Database
def get_gt_pair():
    apklist=[]

    sql = "select DISTINCT app_name from gt_pair" 
    
    curs.execute(sql)
    
    res = curs.fetchall()

    for row in res:
        apklist.append(row)

    return apklist



def get_seq(apklist):
    LSlist=[]
    ESlist=[]
    pathlist=[]
    for apkname in apklist:
        sql = "select app_name, app_path, Lseq, Eseq from gt_pair where app_name='%s'" %apkname

        curs.execute(sql)

        res = curs.fetchall()
        
        for row in res:
            app_name = row[0]
            app_path = row[1]
            Lseq = row[2]
            Eseq = row[3]

            pathlist.append(app_path)
            LSlist.append(Lseq)
            ESlist.append(Eseq)

        app1_path = pathlist[0]
        app2_path = pathlist[1]
        LS1 = LSlist[0]
        LS2 = LSlist[1]
        ES1 = ESlist[0]
        ES2 = ESlist[1]


        diff_LF = distanceDiff(LS1,LS2)
        diff_EF = distanceDiff(ES1,ES2)

        sql_tmp = "INSERT INTO candidate_pair(app_name,app1_path,app2_path,diff_LF,diff_EF) VALUES('{0}','{1}','{2}','{3}','{4}')"

        sql = sql_tmp.format(app_name,app1_path,app2_path,diff_LF,diff_EF)
        curs.execute(sql)
        conn.commit()




#***********************************
#-----------LCS-------------

def LCS(x,y):
    if (len(x) == 0 or len(y) ==0):
        return 0
    else:
        a = x[0]
        b = y[0]
        if ( a == b):
            return LCS(x[1:],y[1:])+1
        else:
            return cxMax( LCS(x[1:],y), LCS(x,y[1:]) )



def cxMax(a,b):
    if (a>=b):
        return a
    else:
        return b 

#-----------LCS-------------


def zxMax(a,b):
    if ( a >= b ):
        return a
    else:
        return b




def distanceDiff(Stra,Strb):
    lista = []
    listb = []

    for i in range(0, len(Stra)):
        lista.append(Stra[i])
    for i in range(0,len(Strb)):
        listb.append(Strb[i])


    len_LCS = LCS(lista,listb)

    len_a = len(Stra)

    len_b = len(Strb)

    dist = 1 - len_LCS/zxMax(len_a,len_b)


    return dist 

    
#*************************************

if __name__ == "__main__":

    apklist=get_gt_pair()

    get_seq(apklist)

    curs.close()
    conn.close()
   

