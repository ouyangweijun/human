#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-03 23:11
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 02-args+kwargs进行拆包.py
# @Desc     : args+kwargs进行拆包


def test2(a, b, *args, **kwargs):
    print("---------")
    print(a)
    print(b)
    print(args)
    print(kwargs)

def test1(a, b, *args, **kwargs):
    # print("---------")
    # print(a)
    # print(b)
    # print(args)
    # print(kwargs)


    m1 = test2(a, b, args, kwargs)  # 想当于test2(11,22,(33,44,55,66),{"name":"oulen","age",18})
    m2 = test2(a, b, *args, kwargs)  # 想当于test2(11,22,33,44,55,66,{"name":"oulen","age",18})
    m3 = test2(a, b, *args, **kwargs)  # 想当于test2(11,22,33,44,55,66,"name":"oulen","age",18)

test1(11,22,33,44,55,66,name="oulen",age=18)