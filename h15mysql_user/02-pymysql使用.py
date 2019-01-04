#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-04 08:57
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 02-pymysql使用.py
# @Desc     : 02-pymysql使用

# Python 中操作 MySQL 步骤
#
# 引入模块
# 在py文件中引入pymysql模块
# from pymysql import *
# Connection 对象
# 用于建立与数据库的连接
#
# 创建对象：调用connect()方法
#
# conn=connect(参数列表)
# 参数host：连接的mysql主机，如果本机是'localhost'
# 参数port：连接的mysql主机的端口，默认是3306
# 参数database：数据库的名称
# 参数user：连接的用户名
# 参数password：连接的密码
# 参数charset：通信采用的编码方式，推荐使用utf8
# 对象的方法
# close()关闭连接
# commit()提交
# cursor()返回Cursor对象，用于执行sql语句并获得结果
# Cursor对象
# 用于执行sql语句，使用频度最高的语句为select、insert、update、delete
# 获取Cursor对象：调用Connection对象的cursor()方法
# cs1=conn.cursor()
# 对象的方法
# close()关闭
# execute(operation [, parameters ])执行语句，返回受影响的行数，主要用于执行insert、update、delete语句，也可以执行create、alter、drop等语句
# fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
# fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
# 对象的属性
# rowcount只读属性，表示最近一次execute()执行后受影响的行数
# connection获得当前连接对象




# 增删改
"""
from pymysql import *

def main():
    # 创建Connection连接
    conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='mysql',charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行insert语句，并返回受影响的行数：添加一条数据
    # 增加
    count = cs1.execute('insert into goods_cates(name) values("硬盘")')
    #打印受影响的行数
    print(count)

    count = cs1.execute('insert into goods_cates(name) values("光盘")')
    print(count)

    # # 更新
    # count = cs1.execute('update goods_cates set name="机械硬盘" where name="硬盘"')
    # # 删除
    # count = cs1.execute('delete from goods_cates where id=6')

    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    conn.commit()

    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()

if __name__ == '__main__':
    main()
# 查询一行数据
from pymysql import *

def main():
    # 创建Connection连接
    conn = connect(host='localhost',port=3306,user='root',password='mysql',database='jing_dong',charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = cs1.execute('select id,name from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    for i in range(count):
        # 获取查询的结果
        result = cs1.fetchone()
        # 打印查询的结果
        print(result)
        # 获取查询的结果

    # 关闭Cursor对象
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()

"""

# 查询多行数据
from pymysql import *

def main():
    # 创建Connection连接
    conn = connect(host='192.168.50.69',port=3316,user='hotdb_cloud',password='hotdb_cloud',database='jing_dong',charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = cs1.execute('select id,name from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    for i in range(count):
        # 获取查询的结果
        result = cs1.fetchone()
        # 打印查询的结果
        print(result)
        # 获取查询的结果

    result = cs1.fetchall()
    print(result)

    # 关闭Cursor对象
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()



