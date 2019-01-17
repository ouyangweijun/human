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
c.executemany('update user_tb set name=%s where user_id=%s',
    (('小孙', 2),
    ('小白', 3),
    ('小猪', 4),
    ('小牛', 5),
    ('小唐', 6)))
# 通过rowcount获取被修改的记录条数
print('修改的记录条数：', c.rowcount)
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
