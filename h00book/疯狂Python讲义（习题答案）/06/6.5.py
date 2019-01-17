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
class Transport:
    def move(self, distance):
        print('我移动了%s千米' % distance)
        
class Car(Transport):
    def __init__(self, name):
        self.name = name

    def move(self, distance):
        print('%s我在马路上开了%s千米' % (self.name, distance))

class Train(Transport):
    def __init__(self, speed):
        self.speed = speed
    def move(self, distance):
        print('我以速度%s在铁轨上走了%s千米' % (self.speed, distance))

class Plain(Transport):
    def fly(self, distance):
        print('我在天空飞了%s千米' % distance)
    
if __name__ == '__main__':
    c = Car('BMW')
    c.move(30.2)

    t = Train(300)
    t.move(230.5)

    p = Plain()
    p.move(3440.8)
    p.fly(3440.8)