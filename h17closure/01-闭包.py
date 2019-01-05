#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-05 10:06
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 01-闭包.py
# @Desc     : 实现闭包的功能


k = 11
b = 12
# 第三种全局变量
def line_2(k,b,x):
    print(k*x+b)

line_2(1,2,0)

# 第四种缺省值

def line_4(x,k=1,b=2):
    print(k*x+b)
line_4(1)

# 第五种，实例对象
class Line5():
    def __init__(self):
        pass

# Line5(1)

#第六种 闭包 嵌套函数的定义使用 就是闭包： 闭包的意义是减少内存的消耗，且
def line_6(k,b):
    def create_y(x):
        print(k*x+b)
    return create_y

line_6_1 = line_6(1,3)
line_6_1(1)

# 思考：函数。匿名函数，闭包，对象， 单做实参 有什么区别

# 函数