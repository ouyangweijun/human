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
from functools import *
class Cell:
    def __init__(self):
        self._alive = False
    # @property装饰器指定该方法可使用属性语法访问
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    # 指定set_alive()方法就是将set_state()方法的state参数指定为True
    set_alive = partialmethod(set_state, True)
    # 指定set_dead()方法就是将set_state()方法的state参数指定为False
    set_dead = partialmethod(set_state, False)
c = Cell()
print(c.alive)
# 相当于调用c.set_state(True)
c.set_alive()
print(c.alive)
# 相当于调用c.set_state(False)
c.set_dead()
print(c.alive)