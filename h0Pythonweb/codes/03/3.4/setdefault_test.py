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
# 设置默认值，该key在dict中不存在，新增key-value对
print(cars.setdefault('PORSCHE', 9.2)) # 9.2
print(cars)
# 设置默认值，该key在dict中存在，不会修改dict内容
print(cars.setdefault('BMW', 3.4)) # 8.5
print(cars)