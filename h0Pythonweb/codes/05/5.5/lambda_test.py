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
def get_math_func(type) :
    result=1
    # 该函数返回的是Lambda表达式
    if type == 'square':
        return lambda n: n * n  # ①
    elif type == 'cube':
        return lambda n: n * n * n  # ②
    else:
        return lambda n: (1 + n) * n / 2 # ③
# 调用get_math_func()，程序返回一个嵌套函数
math_func = get_math_func("cube")
print(math_func(5)) # 输出125
math_func = get_math_func("square")
print(math_func(5)) # 输出25
math_func = get_math_func("other")
print(math_func(5)) # 输出15.0

a = lambda x, y: x + y
def add(x, y): return x+ y