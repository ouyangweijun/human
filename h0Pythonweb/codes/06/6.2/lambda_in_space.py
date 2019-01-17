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
global_fn = lambda p: print('执行lambda表达式，p参数: ', p)
class Category:
    cate_fn = lambda p: print('执行lambda表达式，p参数: ', p)
# 调用全局范围内的global_fn，为参数p传入参数值
global_fn('fkit')  # ①
c = Category()
# 调用类命名空间内的cate_fn，Python自动绑定第一个参数
c.cate_fn()  # ②
