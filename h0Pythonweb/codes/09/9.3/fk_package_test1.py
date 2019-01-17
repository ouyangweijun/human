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
# 导入fk_package包，实际上就是导入包下__init__.py文件
import fk_package
# 导入fk_package包下的print_shape模块，
# 实际上就是导入fk_package目录下的print_shape.py
import fk_package.print_shape
# 实际上就是导入fk_package包（模块）导入print_shape模块
from fk_package import billing
# 导入fk_package包下的arithmetic_chart模块，
# 实际上就是导入fk_package目录下的arithmetic_chart.py
import fk_package.arithmetic_chart

fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)