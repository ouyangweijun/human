#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-03 09:05
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 02-拷贝文件对比.py
# @Desc     :

import copy

a = [11,22]
b = [33,44]
c = [a,b]
d = copy.copy(c)
e = copy.deepcopy(c)

c.append([55,66])
print(c)
print(d)
print(e)
c.remove([11,22])
print(c)
print(d)
print(e)


# 因为元组是不可变类型，因此当元组进行拷贝的时候，其实是直接指向啦原来的文件地址


print("分隔符浅拷贝元组")

a1 = (11,22)
b1 = copy.copy(a1)
print(id(a1))

print(id(b1))

c1 = a1

print(id(c1))

print("分隔符深拷贝元组")

a1 = (11,22)
b1 = copy.copy(a1)
print(id(a1))

print(id(b1))

c1 = a1

print(id(c1))



print("分隔符被拷贝的元组里面的数据有是非元组数据")

# 如果使用copy.copy,copy.deepcopy()
# 全部都是不可变类型，无论是浅拷贝或是是深拷贝，都是应用
# 存在可变类型的时候，使用深拷贝，拷贝全部的数据

a2 = [11,22]
b2 = [33,44]
c2 = (a,b)
d2 = copy.copy(c2)  # 使用浅拷贝依旧之进行拷贝地址，即应用
e2 = copy.deepcopy(c2)  # 但是使用深拷贝的时候，则进行数据的拷贝
print(id(c2))
print(id(d2))
print(id(e2))





# 浅拷贝对不可变类型和可变类型的copy不同
# copy.copy对于可变类型，会进行浅拷贝
# copy.copy对于不可变类型，不会拷贝，仅仅是指向
# In [88]: a = [11,22,33]
# In [89]: b = copy.copy(a)
# In [90]: id(a)
# Out[90]: 59275144
# In [91]: id(b)
# Out[91]: 59525600
# In [92]: a.append(44)
# In [93]: a
# Out[93]: [11, 22, 33, 44]
# In [94]: b
# Out[94]: [11, 22, 33]
#
#
# In [95]: a = (11,22,33)
# In [96]: b = copy.copy(a)
# In [97]: id(a)
# Out[97]: 58890680
# In [98]: id(b)
# Out[98]: 58890680