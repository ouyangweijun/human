#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-04 06:06
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : application.py
# @Desc     :
import config
import tornado.web
from views import index
class Application(tornado.web.Application):
    def __init__(self):
        handles=[
            (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler,{'word1':'good'})
        ]
        super(Application,self).__init__(handles,**config.settings)