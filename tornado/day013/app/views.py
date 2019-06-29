#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-27 23:11
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : views.py
# @Desc     :
import tornado.web
import tornado.websocket

class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        error = ''
        self.render('login.html', error=error)

    def post(self):
        # 获取登录用户信息
        username = self.get_argument('username')
        password = self.get_argument('password')
        # self.get_body_argument()
        # 模拟登陆，校验功能
        if username in ['coco', 'vincent', '大大'] and password == '123456':
            # self.set_cookie('username', username)
            self.set_secure_cookie('username', username)
            self.render('chat.html', username=username)
        else:
            error = '账号或者密码错误'
            self.render('login.html', error=error)




class ChatHandler(tornado.websocket.WebSocketHandler):

    # 用于存放连接的对象
    user_online = []
    def open(self, *args, **kwargs):
        self.user_online.append(self)
        for user in self.user_online:
            # 当进入chat.html页面时，会主动触发该函数
            username = self.get_secure_cookie('username').decode('utf-8')
            # username = self.get_cookie('username')
            user.write_message('系统提示:【%s已进入聊天室】' % username)

    def on_message(self, message):
        # 接收前端传的数据
        username = self.get_cookie('username')
        for user in self.user_online:
            user.write_message('%s:%s' % (username,message))

    def on_close(self):
        # 移除连接对象
        self.user_online.remove(self)
        for user in self.user_online:
            username = self.get_cookie('username')
            user.write_message('系统提示:【%s已退出聊天室】' % username)