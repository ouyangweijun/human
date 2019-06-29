#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-29 19:20
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 01ty.py
# @Desc     :


import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """
    处理主页函数
    """
    def get(self, *args, **kwargs):
        self.write('你好 torando')



if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/index/',IndexHandler)
        ]

    )

    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()