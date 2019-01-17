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
class A:
    pass
class B:
    pass
class C(A, B):
    pass
print('类A的所有父类:', A.__bases__)
print('类B的所有父类:', B.__bases__)
print('类C的所有父类:', C.__bases__)
 
print('类A的所有子类:', A.__subclasses__())
print('类B的所有子类:', B.__subclasses__())
