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
class Fruit:
    def info(self):
        print("我是一个水果！重%g克" % self.weight)

class Food:
    def taste(self):
        print("不同食物的口感不同")

# 定义Apple类，继承了Fruit和Food类
class Apple(Fruit, Food):
    pass

# 创建Apple对象
a = Apple()
a.weight = 5.6
# 调用Apple对象的info()方法
a.info()
# 调用Apple对象的taste()方法
a.taste()