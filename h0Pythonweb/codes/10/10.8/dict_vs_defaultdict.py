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
from collections import defaultdict
my_dict = {}
# 使用int作为defaultdict的default_factory
# 将key不存在时，将会返回int()函数的返回值
my_defaultdict = defaultdict(int)
print(my_defaultdict['a']) # 0
print(my_dict['a']) # KeyError