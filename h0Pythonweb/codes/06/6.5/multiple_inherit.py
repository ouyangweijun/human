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
    def info (self):
        print("Item中方法:", '这是一个商品') 
class Product:
    def info (self):
        print("Product中方法:", '这是一个工业产品')
#class Mouse(Item, Product): # ①
class Mouse(Product, Item): # ①
    pass
m = Mouse()
m.info()
    