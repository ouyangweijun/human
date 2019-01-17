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
a_range = range(10)
# 对a_range执行for表达式
a_list = [x * x for x in a_range]
# a_list集合包含10个元素
print(a_list)
b_list = [x * x for x in a_range if x % 2 == 0]
# a_list集合包含5个元素
print(b_list)
# 使用for表达式创建生成器
c_generator = (x * x for x in a_range if x % 2 == 0)
# 使用for循环迭代生成器
for i in c_generator:
    print(i, end='\t')
print()
d_list = [(x, y) for x in range(5) for y in range(4)]
# d_list列表包含20个元素
print(d_list)
dd_list = []
for x in range(5):
    for y in range(4):
        dd_list.append((x, y))
print(dd_list)
            
e_list = [[x, y, z] for x in range(5) for y in range(4) for z in range(6)]
# 3_list列表包含120个元素
print(e_list)

src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
# 只要y能整除x，就将它们配对在一起
result = [(x, y) for x in src_b for y in src_a if y % x == 0]
print(result)