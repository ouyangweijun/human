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
class Point:
    ''' 描述点的类'''
    def __init__(self, x, y):
        ''' 构造器 '''
        self.x = x
        self.y = y

    def distance(self, other):
        ''' 计算两点之间距离 '''
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def judge_triangle(self, p1, p2):
        ''' 判断3个点组成的三角形 '''
        self_p1 = self.distance(p1)
        self_p2 = self.distance(p2)
        p1_p2 = p1.distance(p2)
        # 如果self_p1的距离最大
        if self_p1 > self_p2 and self_p1 > p1_p2:
            if self_p1 > (self_p2 + p1_p2):
                print('不是三角形')
            else:
                print("钝角三角形") if self_p1 ** 2 > (self_p2 ** 2 + p1_p2 ** 2) \
                    else print("锐角三角形") if self_p1 ** 2 < (self_p2 ** 2 + p1_p2 ** 2) \
                    else print("直角三角形")
        # 如果self_p2的距离最大
        if self_p2 > self_p1 and self_p2 > p1_p2:
            if self_p2 > (self_p1 + p1_p2):
                print('不是三角形')
            else:
                print("钝角三角形") if self_p2 ** 2 > (self_p1 ** 2 + p1_p2 ** 2) \
                    else print("锐角三角形") if self_p2 ** 2 < (self_p1 ** 2 + p1_p2 ** 2) \
                    else print("直角三角形")
        # 如果p1_p2的距离最大
        if p1_p2 > self_p1 and p1_p2 > self_p2:
            if p1_p2 > (self_p1 + self_p2):
                print('不是三角形')
            else:
                print("钝角三角形") if p1_p2 ** 2 > (self_p1 ** 2 + self_p2 ** 2) \
                    else print("锐角三角形") if p1_p2 ** 2 < (self_p1 ** 2 + self_p2 ** 2) \
                    else print("直角三角形")
    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)

if __name__ == '__main__':
    pt = Point(1, 1)
    print(pt.distance(Point(2, 3)))
    pt.judge_triangle(Point(4, 1), Point(5, 5))