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
# ③、执行DDL语句创建数据表
c.execute('''create table user_tb(
	user_id int primary key auto_increment,
	name varchar(255),
	pass varchar(255), 
	gender varchar(255))''')
# 执行DDL语句创建数据表
c.execute('''create table order_tb(
	order_id integer primary key auto_increment,
	item_name varchar(255),
	item_price double,
    item_number double,
	user_id int,
    foreign key(user_id) references user_tb(user_id) )''')
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()
