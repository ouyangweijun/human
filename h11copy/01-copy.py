#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-03 08:54
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 01-copy.py
# @Desc     :

import copy

# 1.浅拷贝
a = [11,22]
b = [33,44]
c = [a,b]
d = c
e = copy.copy(c)

print(id(c))  # 虽然id c 和id e 是不相同的，其实是指向啦当前的 上一层的引用地址
print(id(e))
print(id(c[0]))
print(id(e[0]))

# 2399754315976  id(c)
# 2399754478152  id(e)
# 2399754355272  id(c[0])
# 2399754355272  id(e[0])

# 2.深拷贝
a1 = [11,22]
b1 = [33,44]
c1 = [a1,b1]
d1 = c1
e1 = copy.deepcopy(c1)

print("-----------拷贝分隔符------")

print(id(c1))  # 使用的是deepcopy  是将里面的数据直接复制出来到自己列表里面去
print(id(e1))
print(id(c1[0]))
print(id(e1[0]))
