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
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    def __setattr__(self, name, value):
        print('----设置%s属性----' % name)
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        print('----读取%s属性----' % name)
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError
    def __delattr__(self, name):
        print('----删除%s属性----' % name)
        if name == 'size':
            self.__dict__['width'] = 0
            self.__dict__['height'] = 0
           
rect = Rectangle(3, 4)
print(rect.size)
rect.size = 6, 8
print(rect.width)
del rect.size
print(rect.size)