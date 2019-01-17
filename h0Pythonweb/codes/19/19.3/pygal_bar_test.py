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
# 定义2个列表分别作为两组柱状图的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 创建pygal.Bar对象（柱状图）
bar = pygal.Bar()
# 添加两组代表条柱的数据
bar.add('疯狂Java讲义', y_data)
bar.add('疯狂Android讲义', y_data2)
## 设置X轴的刻度值
#bar.x_labels = x_data
#bar.title = '疯狂图书的历年销量'
## 设置X、Y轴的标题
#bar.x_title = '年份'
#bar.y_title = '销量'
# 指定将数据图输出到SVG文件中
bar.render_to_file('fk_books.svg')
