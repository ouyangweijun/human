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
cnt = Counter()
# 访问并不存在的key，将输出该key的次数为0.
print(cnt['Python']) # 0
for word in ['Swift', 'Python', 'Kotlin', 'Kotlin', 'Swift', 'Go']:
    cnt[word] += 1
print(cnt)
# 只访问Counter对象的元素
print(list(cnt.elements()))
# 将字符串（迭代器）转换成Counter
chr_cnt = Counter('abracadabra')
# 获取出现最多的3个字母
print(chr_cnt.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
# 用Counter对象执行减法，其实就是减少各元素的出现次数
c.subtract(d)
print(c) # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
e = Counter({'x': 2, 'y': 3, 'z': -4})
# 调用del删除key-value对，会真正删除该key-value对
del e['y']
print(e)
# 访问'w'对应的value，'w'没有出现过，因此返回0
print(e['w']) # 0
# 删除e['w']，删除该key-value对
del e['w']
# 再次访问'w'对应的value，'w'还是没有，因此返回0
print(e['w']) # 0

