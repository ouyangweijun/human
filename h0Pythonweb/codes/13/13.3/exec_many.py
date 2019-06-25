# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
# 导入访问MySQL的模块
import mysql.connector

# ①、连接数据库
conn = conn = mysql.connector.connect(user='root', password='32147',
    host='localhost', port='3306',
    database='python', use_unicode=True)
# ②、获取游标
c = conn.cursor()
# ③、调用executemany()方法把同一条SQL语句执行多次
c.executemany('insert into user_tb values(null, %s, %s, %s)',
    (('sun', '123456', 'male'),
    ('bai', '123456', 'female'),
    ('zhu', '123456', 'male'),
    ('niu', '123456', 'male'),
    ('tang', '123456', 'male')))
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
