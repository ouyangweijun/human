#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-05-29 07:14
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : server.py
# @Desc     :



import tornado.web
"""
tornado 的基础模块 web 框架模块
"""

import tornado.ioloop

"""
tornado io 循环模块，封装linux epoll 和 bsd的kqueue,是tornado 高效的基础

"""




# 业务处理类
class IndexHandler(tornado.web.RequestHandler):

# 类比Django 中的视图 函数
# def IndexHandler():

    # 处理get 请求的，不能处理post 请求
    def get(self,*args,**kwargs):
        # 对应http 请求的方法
        # 给浏览器响应信息
        self.write("success")



if __name__ == '__main__':
    # 实例化一个应用的对象，根据对象进行相关操作

    # Application: 是tornado web 框架的核心应用类，是与服务器对应的接口
    # 里面保存路由映射表，有一个监听的方法 listen 方法用来创建一个服务器实例，并且绑定一个端口

    app = tornado.web.Application([(r'/', IndexHandler)])

    # 绑定监听端口，注意：此时的服务器并没有开启监听
    app.listen(8000)

    # start() 方法是开始监听  IOLoop.current()：返回当前线程的IOLoop实例
    # IOLoop.start()：启动IOLoop 实例的I/O循环
    tornado.ioloop.IOLoop.current().start()
