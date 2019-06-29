#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-26 08:02
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : models.py
# @Desc     :
from sqlalchemy import Column,Integer,String

from utils.conn import Base

def create_db():
    # 映射模型对应的表
    Base.metadata.create_all()


def drop_db():
    # 删除模型映射的表
    Base.metadata.drop_all()


class Student(Base):
    # 主键自增的int类型的id主键
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 定义不能为空的唯一的姓名字段
    s_name = Column(String(10), unique=True, nullable=False)
    s_age = Column(Integer, default=18)

    __tablename__ = 'student'

    # def __repr__(self):



