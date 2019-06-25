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
from collections import namedtuple
# 定义命名元组类：Point
Point = namedtuple('Point', ['x', 'y'])
# 初始化Point对象，即可用位置参数，也可用命名参数
p = Point(11, y=22)
# 像普通元组一样用根据索引访问元素
print(p[0] + p[1]) # 33
# 执行元组解包，按元素的位置解包
a, b = p
print(a, b) # 11, 22
# 根据字段名访问各元素
print(p.x + p.y) # 33
print(p) # Point(x=11, y=22)


my_data = ['East', 'North']
# 创建命名元组对象
p2 = Point._make(my_data)
print(p2) # Point(x='East', y='North')
# 将命名元组对象转换成OrderedDict
print(p2._asdict()) # OrderedDict([('x', 'East'), ('y', 'North')])
# 替换命名元组对象的字段值
p2._replace(y='South')
print(p2) # Point(x='East', y='North')
# 输出p2包含的所有字段
print(p2._fields) # ('x', 'y')
# 再次定义一个命名元组类
Color = namedtuple('Color', 'red green blue')
# 再次定义命名元组类，其字段由Point的字段加上Color的字段
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
# 创建Pixel对象，分别为x、y、red、green、blue字段赋值
pix = Pixel(11, 22, 128, 255, 0)
print(pix) # Pixel(x=11, y=22, red=128, green=255, blue=0)