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
import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color = 'red', linewidth = 2.0,
    linestyle = '--', label='疯狂Java讲义年销量')
plt.plot(x_data, y_data2, color = 'blue', linewidth = 3.0,
    linestyle = '-.', label='疯狂Android讲义年销量')
import matplotlib.font_manager as fm
# 使用Matplotlib的字体管理器加载中文字体
my_font=fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf") 
# 调用legend函数设置图例
plt.legend(loc='best')
# 设置两条坐标轴的名字
plt.xlabel("年份")
plt.ylabel("图书销量（本）")
# 设置数据图的标题
plt.title('疯狂图书的历年销量')
# 设置Y轴上的刻度值
# 第一个参数是点的位置，第二个参数是点的文字提示
plt.yticks([50000, 70000, 100000],
    [r'挺好', r'优秀', r'火爆'])
# 调用show()函数显示图形
plt.show()
