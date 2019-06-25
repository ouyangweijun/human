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

# 先定义一个普通类，准备注册为SQL中的自定义聚集函数
class MinLen:
    def __init__(self):
        self.min_len = None
    def step(self, value):
        # 如果self.min_len还未赋值，直接将当前value赋值给self.min_lin
        if self.min_len is None :
            self.min_len = value
            return
        # 找到一个长度更短的value，用value代替self.min_len
        if len(self.min_len) > len(value):
            self.min_len = value
    def finalize(self):
        return self.min_len
# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# 调用create_aggregate注册自定义聚集函数：min_len
conn.create_aggregate('min_len', 1, MinLen)
# ②、获取游标
c = conn.cursor()
# ③、在SQL语句中使用min_len自定义聚集函数
c.execute('select min_len(pass) from user_tb')
print(c.fetchone()[0])
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
