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
data = [[5, 4.0, 5, 5, 5],
    [4.8, 2.8, 4.8, 4.8, 4.9],
    [4.5, 2.9, 4.6, 4.0, 4.9],
    [4.0, 4.8, 4.9, 4.0, 5],
    [3.0, 4.2, 2.3, 3.5, 2],
    [4.8, 4.3, 3.9, 3.0, 4.5]]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python',
    'C#', 'PHP']
# 创建pygal.Radar对象（雷达图）
rader = pygal.Radar()
# 采用循环为雷达图添加数据
for i, per in enumerate(labels):
    rader.add(labels[i], data[i])
rader.x_labels = ['平台健壮性', '语法易用性', '社区活跃度', 
    '市场份额', '未来趋势']
rader.title = '编程语言对比图'
# 控制各数据点的大小
rader.dots_size = 8
# 设置将图例放在底部
rader.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
rader.render_to_file('language_compare.svg')
