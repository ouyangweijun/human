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
# 以初始值（默认为0）为x，以当前序列元素为y，x+y的和作为下一次的初始值
print(reduce(lambda x,y: x + y, range(5))) # 10
print(reduce(lambda x,y: x + y, range(6))) # 15
# 设初始值为10
print(reduce(lambda x,y: x + y, range(6), 10)) # 25
print('----------------')
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'User[name=%s' % self.name
# 定义一个老式的大小比较函数，User的name越长，该User越大
def old_cmp(u1 , u2):
    return len(u1.name) - len(u2.name)
my_data = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]
# 对my_data排序，需要关键字参数（调用cmp_to_key将old_cmp转换为关键字参数
my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print('----------------')
@lru_cache(maxsize=32)
def factorial(n):
    print('~~计算%d的阶乘~~' % n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# 只有这行会计算，然后会缓存5、4、3、2、1的解乘
print(factorial(5))
print(factorial(3))
print(factorial(5))
print('----------------')
# int函数默认将10进制的字符串转换为整数
print(int('12345'))
# 为int函数的base参数指定参数值
basetwo = partial(int, base=2)
basetwo.__doc__ = '将二进制的字符串转换成整数'
# 相当于执行base为2的int()函数
print(basetwo('10010'))
print(int('10010', 2))