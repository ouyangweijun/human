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
import math

class Points:
    ''' 描述点的类 '''
    def __init__(self, x, y, z):
        ''' 构造器 '''
        self.x=x
        self.y=y
        self.z=z
    
    def __sub__(self, no):
        ''' 为减法提供支持的方法 '''
        return  Points((self.x-no.x),(self.y-no.y),(self.z-no.z))

    def dot(self, no):
        ''' 点积 '''
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)

    def cross(self, no):
        ''' 叉积 '''
        return Points((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
if __name__ == '__main__':
    points = list()
    print('请依次输入4个点的x y z（中间以空格隔开）')
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    X = (b - a).cross(c - b)
    Y = (c - b).cross(d - c)
    angle = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))

    print("%.2f" % math.degrees(angle))