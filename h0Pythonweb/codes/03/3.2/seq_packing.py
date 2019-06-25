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
# 序列封包：将10、20、30封装成元组后赋值给vals
vals = 10, 20, 30
print(vals) # (10, 20, 30)
print(type(vals)) # <class 'tuple'>
print(vals[1]) # 20
a_tuple = tuple(range(1, 10, 2))
# 序列解包: 将a_tuple元组的各元素依次赋值给a、b、c、d、e变量
a, b, c, d, e = a_tuple
print(a, b, c, d, e) # 1 3 5 7 9
a_list = ['fkit', 'crazyit']
# 序列解包: 将a_list序列的各元素依次赋值给a_str、b_str变量
a_str, b_str = a_list
print(a_str, b_str) # fkit crazyit


# 将10、20、30依次赋值给x、y、z
x, y, z = 10, 20, 30
print(x, y, z) # 10 20 30
# 将y,z, x依次赋值给x、y、z
x, y, z = y, z, x
print(x, y, z) # 20 30 10

# first、second保存前2个元素，rest列表包含剩下的元素
first, second, *rest = range(10)
print(first) # 0
print(second) # 1
print(rest) # [2, 3, 4, 5, 6, 7, 8, 9]
# last保存最后一个元素，begin保存前面剩下的元素
*begin, last = range(10)
print(begin) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last) # 9
# first保存第一个元素，last保存最后一个元素，middle保存中间剩下的元素
first, *middle, last = range(10)
print(first) # 0
print(middle) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last) # 9
