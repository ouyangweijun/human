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
a_list = ['crazyit', 20, -2.4, (3, 4), 'fkit']
# 删除第3个元素
del a_list[2]
print(a_list) # ['crazyit', 20, (3, 4), 'fkit']
# 删除第2个到第4个（不包含）元素
del a_list[1: 3]
print(a_list) # ['crazyit', 'fkit']
b_list = list(range(1, 10))
# 删除第3个到倒数第2个（不包含）元素，间隔为2
del b_list[2: -2: 2]
print(b_list) # [1, 2, 4, 6, 8, 9]
# 删除第3个到第5个（不包含）元素
del b_list[2: 4]
print(b_list) # [1, 2, 8, 9]

name = 'crazyit'
print(name) # crazyit
# 删除name变量
del name
#print(name) # NameError

c_list = [20, 'crazyit', 30, -4, 'crazyit', 3.4]
# 删除第一次找到的30
c_list.remove(30)
print(c_list) # [20, 'crazyit', -4, 'crazyit', 3.4]
# 删除第一次找到的'crazyit'
c_list.remove('crazyit')
print(c_list) # [20, -4, 'crazyit', 3.4]

c_list.clear()
print(c_list) # []