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
    # 定义__round__方法，程序可调用round()函数将该对象执行四舍五入取整
    def __round__(self, ndigits=0):
        self.width, self.height = round(self.width, ndigits), round(self.height, ndigits)
        return self
    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)
r = Rectangle(4.13, 5.56)
# 对Rectangle对象执行四舍五入取整
result = round(r, 1)
print(r) # Rectangle(width=4.1, height=5.6)
print(result) # Rectangle(width=4.1, height=5.6)