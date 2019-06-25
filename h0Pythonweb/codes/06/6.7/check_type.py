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
# 定义一个字符串
hello = "Hello";
# "Hello"是str类的实例，输出True
print('"Hello"是否是str类的实例: ', isinstance(hello, str))
# "Hello"是object类的子类的实例，输出True
print('"Hello"是否是object类的实例: ', isinstance(hello, object))
# str是object类的子类，输出True
print('str是否是object类的子类: ', issubclass(str, object))
# "Hello"不是tuple类及其子类的实例，输出False
print('"Hello"是否是tuple类的实例: ', isinstance(hello, tuple))
# str不是tuple类的子类，输出False
print('str是否是tuple类的子类: ', issubclass(str, tuple))
# 定义一个列表
my_list = [2, 4]
# [2, 4]是list类的实例，输出True
print('[2, 4]是否是list类的实例: ', isinstance(my_list, list))
# [2, 4]是object类的子类的实例，输出True
print('[2, 4]是否是object类及其子类的实例: ', isinstance(my_list, object))
# list是object类的子类，输出True
print('list是否是object类的子类: ', issubclass(list, object))
# [2, 4]不是tuple类及其子类的实例，输出False
print('[2, 4]是否是tuple类及其子类的实例: ', isinstance([2, 4], tuple))
# list不是tuple类的子类，输出False
print('list是否是tuple类的子类: ', issubclass(list, tuple))

data = (20, 'fkit')
print('data是否为列表或元组: ', isinstance(data, (list, tuple))) # True
# str不是list或者tuple的子类，输出False
print('str是否为list或tuple的子类: ', issubclass(str, (list, tuple)))
# str是list或tuple或object的子类，输出True
print('str是否为list或tuple或object的子类 ', issubclass(str, (list, tuple, object)))


