#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-05 15:19
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 01-待有参数的装饰器.py
# @Desc     :

def set_lever(lever_num):
    def set_func(func):
        def call_func(*args,**kwargs):
            if lever_num == 1:
                print("权限验证等级一")
            if lever_num == 2:
                print("权限等级验证二")
            return func()
        return call_func
    return set_func
@set_lever(1)
def test1():
    print("-----test1-----")
    return "OK1"
@set_lever(2)
def test2():
    print("-----test2----")
    return "ok2"

test1()

# 带有参数的装饰器 其实是三层的嵌套调用，然后是返回函数的引用