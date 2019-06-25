# coding: utf-8
#########################################################################
# 网站: <a href="http:#www.crazyit.org">疯狂Java联盟</a>               #
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
# 使用花括号构建set集合
c = {'白骨精'}
# 添加元素
c.add("孙悟空")
c.add(6)
print("c集合的元素个数为:" , len(c)) # 输出3
# 删除指定元素
c.remove(6)
print("c集合的元素个数为:" , len(c)) # 输出2
# 判断是否包含指定字符串
print("c集合是否包含'孙悟空'字符串:" , ("孙悟空" in c)) # 输出True
c.add("轻量级Java EE企业应用实战")
print("c集合的元素：" , c)
# 使用set()函数（构造器）来创建set集合
books = set()
books.add("轻量级Java EE企业应用实战")
books.add("疯狂Java讲义")
print("books集合的元素：" , books)
# issubset()方法判断是否为子集合
print("books集合是否为c的子集合？", books.issubset(c)) # 输出False
# issubset()方法与<=运算符效果相同
print("books集合是否为c的子集合？", (books <= c)) # 输出False
# issuperset()方法判断是否为父集合
# issubset和issuperset其实就是倒过来判断
print("c集合是否完全包含books集合？", c.issuperset(books)) # 输出False
# issuperset()方法与>=运算符效果相同
print("c集合是否完全包含books集合？", (c >= books)) # 输出False
# 用c集合减去books集合里的元素，不改变c集合本身
result1 = c - books
print(result1)
# difference()方法也是对集合做减法，与用-执行运算的效果完全一样
result2 = c.difference(books)
print(result2)
# 用c集合减去books集合里的元素，改变c集合本身
c.difference_update(books)
print("c集合的元素：" , c)
# 删除c集合里的所有元素
c.clear()
print("c集合的元素：" , c)
# 直接创建包含元素的集合
d = {"疯狂Java讲义", '疯狂Python讲义', '疯狂Kotlin讲义'}
print("d集合的元素：" , d)
# 计算两个集合的交集，不改变d集合本身
inter1 = d & books
print(inter1)
# intersection()方法也是获取两个集合的交集，与用&执行运算的效果完全一样
inter2 = d.intersection(books)
print(inter2)
# 计算两个集合的交集，改变d集合本身
d.intersection_update(books)
print("d集合的元素：" , d)
# 将range对象包装成set集合
e = set(range(5))
f = set(range(3, 7))
print("e集合的元素：" , e)
print("f集合的元素：" , f)
# 对两个集合执行异或运算
xor = e ^ f
print('e和f执行xor的结果：', xor)
# 计算两个集合的并集，不改变e集合本身
un = e.union(f)
print('e和f执行并集的结果：', un)
# 计算两个集合的并集，改变e集合本身
e.update(f)
print('e集合的元素：', e)
