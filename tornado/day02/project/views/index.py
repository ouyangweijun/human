#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-04 05:57
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : index.py
# @Desc     :

import tornado.web
from tornado.web import RequestHandler
# 业务处理类
class IndexHandler(tornado.web.RequestHandler):

# 类比Django 中的视图 函数
# def IndexHandler():

    # 处理get 请求的，不能处理post 请求
    def get(self,*args,**kwargs):
        # 对应http 请求的方法
        # 给浏览器响应信息
        print('11')
        self.write("success")

class HomeHandler(tornado.web.RequestHandler):

# 类比Django 中的视图 函数
# def IndexHandler():

    # 处理get 请求的，不能处理post 请求
    def get(self,*args,**kwargs):
        # 对应http 请求的方法
        # 给浏览器响应信息
        print('11')
        self.write("home ")
