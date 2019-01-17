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
# ③、调用callproc()方法执行存储过程
# 虽然add_pro存储过程需要3个参数，但最后一个参数是传出参数，
# 因此程序不会用它的值
result_args = c.callproc('add_pro', (5, 6, 0))
# 返回的result_args既包含了传入参数的值，也包含了传出参数的值
print(result_args)
# 如果只想访问传出参数的值，可直接访问result_args的第3个元素，如下代码
print(result_args[2])
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
