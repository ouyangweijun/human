#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-05-29 07:14
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : server.py
# @Desc     : 定义全局变量

import tornado.web
"""
tornado 的基础模块 web 框架模块
"""
import tornado.ioloop

"""
tornado io 循环模块，封装linux epoll 和 bsd的kqueue,是tornado 高效的基础

"""
import config
# 导入服务器模块
import tornado.httpserver
from views import index
import application

if __name__ == '__main__':

    # 开启服务器 httpServer 监听对象
    app = application.Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    #httpServer.listen(8000)
    httpServer.bind(config.options['port'])  # 绑定8000端口  将服务器绑定到制定的端口上 没有监听
    httpServer.start(1)  #  启动多进程  线程数量默认开启一个进程 值大于0，创建对应个数的进程  值可以为None 或者是小于等于0 开启对应硬件机器的cpu 核心数个子进程
    tornado.ioloop.IOLoop.current().start()

    # 启动服务器 进行相关服务监听

