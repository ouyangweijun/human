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
import itertools as it
# count(10, 3)生成10、13、16……迭代器
for e in it.count(10, 3):
    print(e)
    # 用于跳出无限循环
    if e > 20:
        break
print('---------')
my_counter = 0
# cycle用于对序列生成无限循环的迭代器
for e in it.cycle(['Python', 'Kotlin', 'Swift']):
    print(e)
    # 用于跳出无限循环
    my_counter += 1
    if my_counter > 7:
        break
print('---------')
# repeat用于生成n个元素重复的迭代器
for e in it.repeat('Python', 3):
    print(e)
    
    
