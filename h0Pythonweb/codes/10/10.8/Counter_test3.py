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
# 创建Counter对象
c = Counter(Python=4, Swift=2, Kotlin=3, Go=-2)
# 统计Counter中所有出现次数的总和
print(sum(c.values())) # 7
# 将Counter转换为list，只保留各key
print(list(c)) # ['Python', 'Swift', 'Kotlin', 'Go']
# 将Counter转换为set，只保留各key
print(set(c)) # {'Go', 'Python', 'Swift', 'Kotlin'}
# 将Counter转换为dict
print(dict(c)) # {'Python': 4, 'Swift': 2, 'Kotlin': 3, 'Go': -2}
# 将Counter转换为list，列表元素都是(元素, 出现次数)组
list_of_pairs = c.items()
print(list_of_pairs) # dict_items([('Python', 4), ('Swift', 2), ('Kotlin', 3), ('Go', -2)])
# 将列表元素为(元素, 出现次数)组的list转换成Counter
c2 = Counter(dict(list_of_pairs))
print(c2) # Counter({'Python': 4, 'Kotlin': 3, 'Swift': 2, 'Go': -2})
# 获取Counter中最少出现的3个元素
print(c.most_common()[:-4:-1]) # [('Go', -2), ('Swift', 2), ('Kotlin', 3)]
# 清空所有key-value对
c.clear()
print(c) # Counter()
c = Counter(a=3, b=1, c=-1)
d = Counter(a=1, b=-2, d=3)
# 对Counter执行加法
print(c + d)  # Counter({'a': 4, 'd': 3})
# 对Counter执行减法
print(c - d)  # Counter({'b': 3, 'a': 2})
Counter({'a': 2})
# 对Counter执行交运算
print(c & d) # Counter({'a': 1})
print(c | d) # Counter({'a': 3, 'd': 3, 'b': 1}) 
print(+c) # Counter({'a': 3, 'b': 1})
print(-d) # Counter({'b': 2})