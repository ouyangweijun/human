#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-05 01:25
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : mini_fram.py
# @Desc     : WSGI 实现

def index():
    return "这是主要的页面"

def login():
    return "这是登陆页面"
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    file_name = environ["PATH_INFO"]
    # file_name = "/index.html"
    print("-------------")
    print(file_name)
    if file_name == '/index.py':
        return index()
    if file_name == '/login.py':
        return login()
    else:
        return '<h1>Hello,web!,我爱你中国!</h1>'