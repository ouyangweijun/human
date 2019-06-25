# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
from functools import *
@singledispatch
def test(arg, verbose):
    if verbose:
        print("默认参数为：", end=" ")
    print(arg)
# 限制test函数第一个参数为int型的函数版本
@test.register(int)
def _(argu, verbose):
    if verbose:
        print("整型参数为：", end=" ")
    print(argu)
test('Python', True)  # ①
# 调用第一个参数为int型的版本
test(20, True)  # ②
# 限制test函数第一个参数为list型的函数版本
@test.register(list)
def _(argb, verbose=False):
    if verbose:
        print("列表中所有元素为:")
    for i, elem in enumerate(argb):
        print(i, elem, end=" ")
test([20, 10, 16, 30, 14], True) # ③
print("\n---------------") 
# 定义一个函数，不使用函数装饰器修饰
def nothing(arg, verbose=False):
    print("~~None参数~~")
# 当test函数第一个参数为None类型时，转向为调用nothing函数
test.register(type(None), nothing)
test(None, True) # ④
print("\n---------------") 

from decimal import Decimal
# 限制test函数第一个参数为float或Decimal型的函数版本
@test.register(float)
@test.register(Decimal)
def test_num(arg, verbose=False):
    if verbose:
        print("参数的一半为:", end=" ")
    print(arg / 2)
# test.dispatch(类型)即可获取它转向的函数
# 当test()函数第一个参数为float时将转向到调用test_num
print(test_num is test.dispatch(float)) # True
# 当test()函数第一个参数为Decimal时将转向到调用test_num
print(test_num is test.dispatch(Decimal)) # True
# 直接调用test并不等于test_num
print(test_num is test) # False

# 获取test函数所绑定的全部类型
print(test.registry.keys())
# 获取test函数为int类型绑定的函数
print(test.registry[int])