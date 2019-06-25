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
# 导入访问SQLite的模块
import sqlite3

# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# ②、获取游标
c = conn.cursor()
# ③、调用执行select语句查询数据
c.execute('select * from user_tb where _id > ?', (2,))
# 通过游标的description属性获取列信息
for col in (c.description):
    print(col[0], end='\t')
print('\n--------------------------------')
while True:
    # 每次抓取3条记录，该方法返回一个由3条记录组成的列表
    rows = c.fetchmany(3)
    # 如果抓取的rows为None，退出循环
    if not rows :
        break
    # 再次使用循环遍历获取的列表
    for r in rows:
        print(r)
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
