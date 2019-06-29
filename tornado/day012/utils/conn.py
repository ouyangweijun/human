#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-26 23:30
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : conn.py
# @Desc     :


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 连接数据库格式
# mysql+pymysql://root:123456@127.0.0.1:3306/tornado9
db_url = 'mysql+pymysql://oulen:7989264@127.0.0.1:3306/flask9'

# 创建引擎，建立连接
engine = create_engine(db_url)

# 模型与数据库表进行关联的基类，模型必须继承于Base
Base = declarative_base(bind=engine)

# 创建session会话
DbSession = sessionmaker(bind=engine)
session = DbSession()




