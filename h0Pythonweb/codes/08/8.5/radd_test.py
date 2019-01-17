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
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 定义setSize()函数
    def setSize (self , size):
        self.width, self.height = size
    # 定义getSize()函数
    def getSize (self):
        return self.width, self.height
    # 使用property定义属性
    size = property(getSize, setSize)
    # 定义__radd__方法，该对象可出现在+的右边
    def __radd__(self, other):
        # 要求参与+运算的另一个运算数必须是数值
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('+运算要求目标是数值')
        return Rectangle(self.width + other, self.height + other)
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)
r1 = Rectangle(4, 5)
# r1有__radd__方法，因此它可以出现在+运算符的右边
r = 3 + r1
print(r) # Rectangle(width=7, height=8)
