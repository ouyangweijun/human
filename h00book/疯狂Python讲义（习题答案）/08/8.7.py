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
class Point(object):
    ''' 描述点的类 '''
    def __init__(self, x, y):
        ''' 构造器 '''
        self.x=x
        self.y=y
    
    def __sub__(self, no):
        ''' 为减法提供支持的方法 '''
        return ((self.x - no.x) ** 2 + (self.y - no.y) ** 2) ** 0.5

if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(5, 6)
    print(p1 - p2)
    print(p2 - p1)
