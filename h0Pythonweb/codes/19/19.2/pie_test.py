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

# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992, 
    0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python',
    'Visual Basic .NET', 'C#', 'PHP', 'JavaScript',
    'SQL', 'Assembly langugage', '其他']
# 将第4个语言（Python）分离出来
explode = [0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0]
# 使用自定义颜色
colors=['red', 'pink', 'magenta','purple','orange'] 
# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')
# 控制X轴和Y轴的范围（用于控制饼图的圆心，半径）
plt.xlim(0,8)
plt.ylim(0,8)

# 绘制饼图
plt.pie(x = data, # 绘图数据
    labels=labels, # 添加编程语言标签
    explode=explode, # 突出显示Python
    colors=colors, # 设置饼图的自定义填充色
    autopct='%.3f%%', # 设置百分比的格式，此处保留3位小数
    pctdistance=0.8,  # 设置百分比标签与圆心的距离
    labeldistance = 1.15, # 设置标签与圆心的距离
    startangle = 180, # 设置饼图的初始角度
    center = (4, 4), # 设置饼图的圆心（相当于X轴和Y轴的范围）
    radius = 3.8, # 设置饼图的半径（相当于X轴和Y轴的范围）
    counterclock = False, # 是否逆时针，这里设置为顺时针方向
    wedgeprops = {'linewidth': 1, 'edgecolor':'green'},# 设置饼图内外边界的属性值
    textprops = {'fontsize':12, 'color':'black'}, # 设置文本标签的属性值
    frame = 1) # 是否显示饼图的圆圈，此处设为显示
# 不显示X轴和Y轴的刻度值
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('2018年8月的编程语言指数排行榜')
# 显示图形
plt.show()