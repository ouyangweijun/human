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
im = Item('鼠标', 28.9)
print(im.__dict__)  # ①
# 通过__dict__访问name属性
print(im.__dict__['name'])
# 通过__dict__访问price属性
print(im.__dict__['price'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 32.8
print(im.name) # 键盘
print(im.price) # 32.8