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
# ③、调用executemany()方法把同一条SQL语句执行多次
c.executemany('update user_tb set name=? where _id=?',
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
