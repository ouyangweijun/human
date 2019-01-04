#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-04 07:53
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 01-使用数据库.py
# @Desc     : MySQL数据库使用



# RDBMS
# Relational Database Management System
#
# 通过表来表示关系型
#
# 当前主要使用两种类型的数据库：关系型数据库、非关系型数据库，本部分主要讨论关系型数据库，对于非关系型数据库会在后面学习
#
# 所谓的关系型数据库RDBMS，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据
#
# 查看数据库排名:https://db-engines.com/en/ranking
#
# 关系型数据库的主要产品：
#
# oracle：在以前的大型项目中使用,银行,电信等项目
# mysql：web时代使用最广泛的关系型数据库
# ms sql server：在微软的项目中使用
# sqlite：轻量级数据库，主要应用在移动平台




# SQL
# Structured Query Language
#
# SQL是结构化查询语言，是一种用来操作RDBMS的数据库语言，当前关系型数据库都支持使用SQL语言进行操作,也就是说可以通过 SQL 操作 oracle,sql server,mysql,sqlite 等等所有的关系型的数据库
#
# SQL语句主要分为：
# DQL：数据查询语言，用于对数据进行查询，如select
# DML：数据操作语言，对数据进行增加、修改、删除，如insert、udpate、delete
# TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback
# DCL：数据控制语言，进行授权与权限回收，如grant、revoke
# DDL：数据定义语言，进行数据库、表的管理等，如create、drop
# CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor
# 对于web程序员来讲，重点是数据的crud（增删改查），必须熟练编写DQL、DML，能够编写DDL完成数据库、表的操作，其它语言如TPL、DCL、CCL了解即可
# SQL 是一门特殊的语言,专门用来操作关系数据库
# 不区分大小写
# 学习要求
# 熟练掌握数据增删改查相关的 SQL 语句编写
# 在 Python代码中操作数据就是通过 SQL 语句来操作数据
# 创建Connection连接
conn = connect(host='localhost', port=3306, user='root', password='mysql', database='python1', charset='utf8')
# 得Cursor对象
cs = conn.cursor()
# 更新
# sql = 'update students set name="刘邦" where id=6'
# 删除
# sql = 'delete from students where id=6'
# 执行select语句，并返回受影响的行数：查询一条学生数据
sql = 'select id,name from students where id = 7'
# sql = 'SELECT id,name FROM students WHERE id = 7'
count=cs.execute(sql)
# 打印受影响的行数
print(count)