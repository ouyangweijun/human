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
class Item:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
    def info ():
        pass
# 创建一个Item对象，将之赋给im变量
im = Item('鼠标', 29.8)
print(im.__dir__())  # 返回所有属性（包括方法）组成列表
print(dir(im))  # 返回所有属性（包括方法）排序之后的列表
