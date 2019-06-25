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
from heapq import *
my_data = list(range(10))
my_data.append(0.5)
# 此时my_data依然是一个list列表
print('my_data的元素：', my_data)
# 对my_data应用堆属性
heapify(my_data) 
print('应用堆之后my_data的元素：', my_data)
heappush(my_data, 7.2)
print('添加7.2之后my_data的元素：', my_data)
# 弹出堆中最小的元素
print(heappop(my_data)) # 0
print(heappop(my_data)) # 0.5
print('弹出两个元素之后my_data的元素：', my_data)
# 弹出最小元素，压入指定元素
print(heapreplace(my_data, 8.1))
print('执行replace之后my_data的元素：', my_data)
print('my_data中最大的3个元素：', nlargest(3, my_data))
print('my_data中最小的4个元素：', nsmallest(4, my_data))


