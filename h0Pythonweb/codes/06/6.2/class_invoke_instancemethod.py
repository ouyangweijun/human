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
class User:
    def walk (self):
        print(self, '正在慢慢地走')
# 通过类调用实例方法
#User.walk()
u = User()
# 显式为方法的第一个参数绑定参数值
User.walk(u)

# 显式为方法的第一个参数绑定fkit字符串参数值
User.walk('fkit')