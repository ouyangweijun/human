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
class Canvas:
    def draw_pic(self, shape):
        print('--开始绘图--')
        shape.draw(self)

class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制矩形' % canvas)
class Triangle:
    def draw(self, canvas):
        print('在%s上绘制三角形' % canvas)
class Circle:
    def draw(self, canvas):
        print('在%s上绘制圆形' % canvas)
c = Canvas()
# 传入Rectangle参数，绘制矩形
c.draw_pic(Rectangle())
# 传入Triangle参数，绘制三角形
c.draw_pic(Triangle())
# 传入Circle参数，绘制圆形
c.draw_pic(Circle())
print(hasattr(c, 'draw_pic'))
print(hasattr(c.draw_pic, '__call__'))
print(Circle.__dict__)