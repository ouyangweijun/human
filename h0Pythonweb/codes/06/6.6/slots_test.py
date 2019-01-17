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
class Dog:
    __slots__ = ('walk', 'age', 'name')
    def __init__(self, name):
        self.name = name
    def test():
        print('预先定义的test方法')
d = Dog('Snoopy')
from types import MethodType
# 只允许动态为实例添加walk、age、name这3个属性或方法
d.walk = MethodType(lambda self: print('%s正在慢慢地走' % self.name), d)
d.age = 5
d.walk()
#d.foo = 30 # AttributeError
# __slots__属性并不限制通过类来动态添加方法
Dog.bar = lambda self: print('abc') # AttributeError
d.bar()

class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    pass
gd = GunDog('Puppy')
# 完全可以为Gundog实例动态添加属性
gd.speed = 99
print(gd.speed)
