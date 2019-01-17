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

a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
# 访问从第2个到倒数第4个（不包含）所有元素
print(a_tuple[1: 3]) # (20, 5.6)
# 访问从倒数第3个到倒数第1个（不包含）所有元素
print(a_tuple[-3: -1]) # (5.6, 'fkit')
# 访问从第2个到倒数第2个（不包含）所有元素
print(a_tuple[1: -2]) # (20, 5.6)
# 访问从倒数第3个到第5个（不包含）所有元素
print(a_tuple[-3: 4]) # (5.6, 'fkit')


b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 访问从第3个到第9个（不包含）、间隔为2的所有元素
print(b_tuple[2: 8: 2]) # (3, 5, 7)
# 访问从第3个到第9个（不包含）、间隔为3的所有元素
print(b_tuple[2: 8: 3]) # (3, 6)
# 访问从第3个到倒数第2个（不包含）、间隔为3的所有元素
print(b_tuple[2: -2: 2]) # (3, 5, 7)
