#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-27 07:35
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : sync_tornado.py
# @Desc     :



import tornado.web
import tornado.ioloop
import tornado.httpclient


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        # 路由中传递的参数，/index/?q=python
        q = self.get_argument('q=python')
        # 向地址发送请求: https://cn.bing.com/search?q=
        client = tornado.httpclient.HTTPClient()
        response = client.fetch('https://cn.bing.com/search?q=%s' % q)
        print(response)
        self.write('同步测试')


def make_app():

    return tornado.web.Application(handlers=[
        (r'/index/',IndexHandler),
    ])



if __name__ == '__main__':
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
