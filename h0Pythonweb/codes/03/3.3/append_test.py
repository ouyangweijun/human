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
a_list = ['crazyit', 20, -2]
# 追加元素
a_list.append('fkit')
print(a_list) # ['crazyit', 20, -2, 'fkit']
a_tuple = (3.4, 5.6)
# 追加元组，元组被当成一个元素
a_list.append(a_tuple)
print(a_list) # ['crazyit', 20, -2, 'fkit', (3.4, 5.6)]
# 追加列表，列表被当成一个元素
a_list.append(['a', 'b'])
print(a_list) # ['crazyit', 20, -2, 'fkit', (3.4, 5.6), ['a', 'b']]

b_list = ['a', 30]
# 追加元组中的所有元素
b_list.extend((-2, 3.1))
print(b_list) # ['a', 30, -2, 3.1]
# 追加列表中的所有元素
b_list.extend(['C', 'R', 'A'])
print(b_list) # ['a', 30, -2, 3.1, 'C', 'R', 'A']
# 追加区间中的所有元素
b_list.extend(range(97, 100))
print(b_list) # ['a', 30, -2, 3.1, 'C', 'R', 'A', 97, 98, 99]

c_list = list(range(1, 6))
print(c_list) # [1, 2, 3, 4, 5]
# 在索引3处插入字符串
c_list.insert(3, 'CRAZY' )
print(c_list) # [1, 2, 3, 'CRAZY', 4, 5]
# 在索引3处插入元组，元组被当成一个元素
c_list.insert(3, tuple('crazy'))
print(c_list) # [1, 2, 3, ('c', 'r', 'a', 'z', 'y'), 'CRAZY', 4, 5]