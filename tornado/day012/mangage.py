#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-26 07:31
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : mangage.py.py
# @Desc     :


import tornado.web
import os

import pymysql

import tornado.ioloop
import tornado.web
from tornado.options import define,options,parse_config_file,parse_command_line

from app.views import IndexHandler,XindexHandle


define('port',default=80,type=int)


def make_app():

    return tornado.web.Application(handlers=
    [
        (r'/',IndexHandler),
        (r'/index/',XindexHandle)


    ],
        template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
        static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')

    )

if __name__ == '__main__':
    app  = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
