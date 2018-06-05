#!/usr/bin/env python
# coding=utf-8

import os
import conf
import MySQLdb


#
# -------------------------
# Database connection
# -------------------------

def connect_db():
    con = MySQLdb.connect(
        host = conf.DB_HOST,
        user = conf.DB_USER,
        passwd = conf.DB_PASSWD,
        db = conf.DB_NAME,
        charset = 'utf8')
    return con 

