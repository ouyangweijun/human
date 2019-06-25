# coding: utf-8
#########################################################################
# 网站: <a href="http:#www.crazyit.org">疯狂Java联盟</a>               #
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
    # 定义一个计算平方的局部函数
    def square(n) :  # ①
        return n * n
    # 定义一个计算立方的局部函数
    def cube(n) :  # ②
        return n * n * n
    # 定义一个计算阶乘的局部函数
    def factorial(n) :   # ③
        result = 1
        for index in range(2 , n + 1): 
            result *= index
        return result
    # 返回局部函数
    if type == "square" :
        return square
    if type == "cube" :
        return cube
    else:
        return factorial
# 调用get_math_func()，程序返回一个嵌套函数
math_func = get_math_func("cube") # 得到cube函数
print(math_func(5)) # 输出125
math_func = get_math_func("square") # 得到square函数
print(math_func(5)) # 输出25
math_func = get_math_func("other") # 得到factorial函数
print(math_func(5)) # 输出120
