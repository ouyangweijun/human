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

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 创建pygal.StackedBar对象（叠加折线图）
stacked_line = pygal.StackedLine()
# 添加两组数据
stacked_line.add('疯狂Java讲义', y_data)
stacked_line.add('疯狂Android讲义', y_data2)
# 设置X轴的刻度值
stacked_line.x_labels = x_data
# 重新设置Y轴的刻度值
stacked_line.y_labels = [20000, 40000, 60000, 80000, 100000]
stacked_line.title = '疯狂图书的历年销量'
# 设置X、Y轴的标题
stacked_line.x_title = '销量'
stacked_line.y_title = '年份'
# 设置将图例放在底部
stacked_line.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
stacked_line.render_to_file('fk_books.svg')
