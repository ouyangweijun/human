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
# ③、调用执行select语句查询数据
c.execute('select * from user_tb where user_id > %s', (2,))
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------------')
# 直接使用for循环来遍历游标中的结果集
for row in c:
    print(row)
    print(row[1] + '-->' + row[2])
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
