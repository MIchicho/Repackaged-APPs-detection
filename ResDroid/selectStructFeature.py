#!/usr/bin/env python
# coding=utf-8
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
    sql = "select app_path from layout_event"

    curs.execute(sql)

    res = curs.fetchall()

    for row in res:
        app_path = row[0]

        cmd = "echo {0} >> structout.txt".format(app_path)
        os.system(cmd)
        
