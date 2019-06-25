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
from functools import *
#@total_ordering
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'User[name=%s' % self.name
    # 根据是否有name属性来决定是否可比较
    def _is_valid_operand(self, other):
        return hasattr(other, "name")
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        # 根据name判断是否相等（都转成小写比较、忽略大小写）
        return self.name.lower()  == other.lastname.lower()
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        # 根据name判断是否相等（都转成小写比较、忽略大小写）
        return self.lastname.lower() < other.lastname.lower()
# 打印被装饰之后的User类中的__gt__方法
print(User.__gt__)