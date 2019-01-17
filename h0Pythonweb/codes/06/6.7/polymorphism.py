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
class Bird:
    def move(self, field):
        print('鸟在%s上自由地飞翔' % field)
class Dog:
    def move(self, field):
        print('狗在%s里飞快的奔跑' % field)
# x变量被赋值为Bird对象
x = Bird()
# 调用x变量的move()方法
x.move('天空')
# x变量被赋值为Dog对象
x = Dog()
# 调用x变量的move()方法
x.move('草地')
