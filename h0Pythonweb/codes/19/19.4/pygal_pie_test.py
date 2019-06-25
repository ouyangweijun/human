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
import pygal

# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992, 
    0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python',
    'Visual Basic .NET', 'C#', 'PHP', 'JavaScript',
    'SQL', 'Assembly langugage', '其他']
# 创建pygal.Pie对象（饼图）
pie = pygal.Pie()
# 采用循环为饼图添加数据
for i, per in enumerate(data):
    pie.add(labels[i], per)
pie.title = '2018年8月编程语言'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 设置内圈的半径长度
pie.inner_radius = 0.4
# 创建半圆数据图
pie.half_pie = True
# 指定将数据图输出到SVG文件中
pie.render_to_file('language_percent.svg')
