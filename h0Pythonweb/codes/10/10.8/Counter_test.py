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
from collections import Counter
# 创建空的Counter对象
c1 = Counter()
# 以可迭代对象创建Counter对象
c2 = Counter('hannah')
print(c2)
# 以可迭代对象创建Counter对象
c3 = Counter(['Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'Python'])
print(c3)
# 以dict来创建Counter对象
c4 = Counter({'red': 4, 'blue': 2})
print(c4)
# 使用关键字参数的语法创建Counter
c5 = Counter(Python=4, Swift=8)
print(c5)