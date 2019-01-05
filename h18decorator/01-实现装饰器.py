#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-05 11:30
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 01-实现装饰器.py
# @Desc     : 实现装饰器


def set_func(func):
    def call_func():
        print("111111111")
        print("2222222222")
        func()
    return call_func
@set_func
def test1():
    print("111111test111")
test1()