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
a_list = [2, 30, 'a', 'b', 'crazyit', 30]
# 定位元素30的出现位置
print(a_list.index(30)) # 1
# 从索引2处开始、定位元素30的出现位置
print(a_list.index(30, 2)) # 5
# 从索引2处到索引4处之间定位元素30的出现位置，找不到该元素
print(a_list.index(30, 2, 4)) # ValueError
