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
class BaseClass:
    def foo (self):
        print('父类中定义的foo方法')
class SubClass(BaseClass):
    # 重写父类的foo方法
    def foo (self):
        print('子类重写父类中的foo方法')
    def bar (self):
        print('执行bar方法')
        # 直接执行foo方法，将会调用子类重写之后的foo()方法
        self.foo() 
        # 使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        BaseClass.foo(self)
sc = SubClass()
sc.bar()
