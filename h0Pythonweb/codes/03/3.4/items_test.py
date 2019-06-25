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
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 获取字典所有的key-value对，返回一个dict_items对象
ims = cars.items()
print(type(ims)) # <class 'dict_items'>
# 将dict_items转换成列表
print(list(ims)) # [('BMW', 8.5), ('BENS', 8.3), ('AUDI', 7.9)]
# 访问第2个key-value对
print(list(ims)[1]) # ('BENS', 8.3)
# 获取字典所有的key，返回一个dict_keys对象
kys = cars.keys()
print(type(kys)) # <class 'dict_keys'>
# 将dict_keys转换成列表
print(list(kys)) # ['BMW', 'BENS', 'AUDI']
# 访问第2个key
print(list(kys)[1]) # 'BENS'
# 获取字典所有的value，返回一个dict_values对象
vals = cars.values()
# 将dict_values转换成列表
print(type(vals)) # [8.5, 8.3, 7.9]
# 访问第2个value
print(list(vals)[1]) # 8.3
