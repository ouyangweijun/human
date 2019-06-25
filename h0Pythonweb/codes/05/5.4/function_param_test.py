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
# 定义函数类型的形参，其中fn是一个函数
def map(data, fn) :    
    result = []
    # 遍历data列表中每个元素，并用fn函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for e in data :
        result.append(fn(e))
    return result
# 定义一个计算平方的函数
def square(n) :
    return n * n
# 定义一个计算立方的函数
def cube(n) :
    return n * n * n
# 定义一个计算阶乘的函数
def factorial(n) :
    result = 1
    for index in range(2, n + 1) :
        result *= index
    return result
data = [3 , 4 , 9 , 5, 8]
print("原数据: ", data)
# 下面程序代码3次调用map()函数，每次调用时传入不同的函数
print("计算数组元素的平方")
print(map(data , square))
print("计算数组元素的立方")
print(map(data , cube))
print("计算数组元素的阶乘")
print(map(data , factorial))
# 获取map的类型
print(type(map))