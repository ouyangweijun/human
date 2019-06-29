#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-26 07:35
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : views.py
# @Desc     :


import tornado.web
from app.models import create_db, drop_db, Student

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print('hh')
        self.write('hello day tornado')

class XindexHandle(tornado.web.RequestHandler):

    def get(self):
        # 页面渲染
        items = ['Python', 'Php', 'C++', '精通']
        self.render('index.html', items=items, items2=items)


class Dbhandle(tornado.web.RequestHandler):
    def get(self):
        create_db()
