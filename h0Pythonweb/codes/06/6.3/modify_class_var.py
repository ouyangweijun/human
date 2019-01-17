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
class Inventory:
    # 定义两个类变量
    item = '鼠标'
    quantity = 2000
    # 定义实例方法
    def change(self, item, quantity):
        # 下面赋值语句不是对类变量赋值，而是定义新的实例变量
        self.item = item
        self.quantity = quantity
# 创建Inventory对象
iv = Inventory()
iv.change('显示器', 500)
# 访问iv的item和quantity实例变量
print(iv.item) # 显示器
print(iv.quantity) # 500
# 访问Inventory的item和quantity类变量
print(Inventory.item) # 鼠标
print(Inventory.quantity) # 2000

Inventory.item = '类变量item'
Inventory.quantity = '类变量quantity'
# 访问iv的item和quantity实例变量
print(iv.item)
print(iv.quantity)

iv.item = '实例变量item'
iv.quantity = '实例变量quantity'
print(Inventory.item)
print(Inventory.quantity)