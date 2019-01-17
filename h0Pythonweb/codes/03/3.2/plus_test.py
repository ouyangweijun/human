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
a_tuple = ('crazyit' , 20, -1.2)
b_tuple = (127, 'crazyit', 'fkit', 3.33)
# 计算元组相加
sum_tuple = a_tuple + b_tuple
print(sum_tuple) # ('crazyit', 20, -1.2, 127, 'crazyit', 'fkit', 3.33)
print(a_tuple) # a_tuple并没有改变
print(b_tuple) # b_tuple并没有改变
# 两个元组相加
print(a_tuple + (-20 , -30)) # ('crazyit', 20, -1.2, -20, -30)
# 下面代码报错：元组和列表不能直接相加
#print(a_tuple + [-20 , -30])
a_list = [20, 30, 50, 100]
b_list = ['a', 'b', 'c']
# 计算列表相加
sum_list = a_list + b_list
print(sum_list) # [20, 30, 50, 100, 'a', 'b', 'c']
print(a_list + ['fkit']) # [20, 30, 50, 100, 'fkit']
