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
class Cat:
    def __init__(self, name):
        self.name = name
def walk_func(self):
    print('%s慢慢地走过一片草地' % self.name)
d1 = Cat('Garfield')
d2 = Cat('Kitty')
#d1.walk() # AttributeError
# 为Cat动态添加walk()方法，该方法的第一个参数会自动绑定
Cat.walk = walk_func  # ①
# d1、d2调用walk()方法
d1.walk()
d2.walk()
    