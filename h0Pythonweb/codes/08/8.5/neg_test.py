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
    # 定义__neg__方法，该对象可执行求负（-）运算
    def __neg__(self):
        self.width, self.height = self.height, self.width
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)
r = Rectangle(4, 5)
# 对Rectangle执行求负运算
-r
print(r) # Rectangle(width=5, height=4)
