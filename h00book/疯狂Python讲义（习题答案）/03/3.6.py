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
import random

length = int(input("请输入列表的长度:"))
my_list = []
for i in range(length):
    my_list.append(input('请输入字符串:'))
print(my_list)
new_list = []
[new_list.append(i) for i in my_list if not i in new_list]
print(new_list)

# 另一种方法
new_list = list({}.fromkeys(my_list).keys())
print(new_list)