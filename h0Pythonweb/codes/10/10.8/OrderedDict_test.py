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
from collections import OrderedDict
# 创建OrderedDict对象
dx = OrderedDict(b=5, c=2, a=7)
print(dx) # OrderedDict([('b', 5), ('c', 2), ('a', 7)])
d = OrderedDict()
# 向OrderedDict中添加key-value对
d['Python'] = 89
d['Swift'] = 92
d['Kotlin'] = 97
d['Go'] = 87
# 遍历OrderedDict的key-value对
for k,v in d.items():
    print(k, v)

# 创建普通的dict对象
my_data = {'Python': 20, 'Swift':32, 'Kotlin': 43, 'Go': 25}
# 创建基于key排序的OrderedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
# 创建基于value排序的OrderedDict
d2 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(d1) # OrderedDict([('Go', 25), ('Kotlin', 43), ('Python', 20), ('Swift', 32)])
print(d2) # OrderedDict([('Python', 20), ('Go', 25), ('Swift', 32), ('Kotlin', 43)])
print(d1 == d2) # False