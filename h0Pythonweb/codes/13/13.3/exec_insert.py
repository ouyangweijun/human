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
# ③、调用执行insert语句插入数据
c.execute('insert into user_tb values(null, %s, %s, %s)',
    ('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values(null, %s, %s, %s, %s)',
    ('鼠标', '34.2', '3', 1))
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
