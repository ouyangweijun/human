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
class Sums:
    def __init__(self, len):
        self.current_index = 1
        self.current_value = 0
        self.__len = len
    # 定义迭代器所需的__next__方法
    def __next__(self):
        if self.__len == 0:
            raise StopIteration
        # 完成数列计算：
        self.current_value += self.current_index
        self.current_index += 1
        # 数列长度减1
        self.__len -= 1
        return self.current_value
    # 定义__iter__方法，该方法返回迭代器
    def __iter__(self):
        return self
sums = Sums(10)
# 获取迭代器的下一个元素
print(next(sums))
for el in sums:
    print(el, end=' ')
