#!/usr/bin/env python3
# coding:utf-8

import pymysql

# url = 'mysql://root:Qazwsx@123@192.168.199.163:3306/flask'
conn = pymysql.Connection(host='192.168.199.163', port=3306, user='root', password='Qazwsx@123', db='flask')
# conn = pymysql.Connection(url)
cursor = conn.cursor()
sql = 'select * from user'

count = cursor.execute(sql)
ret = cursor.fetchall()

