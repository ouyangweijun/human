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
def fn(self):
    print('fn函数')
# 使用type()定义Dog类
Dog = type('Dog', (object,), dict(walk=fn, age=6))
# 创建Dog对象
d = Dog()
# 分别查看d、Dog的类型
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)
