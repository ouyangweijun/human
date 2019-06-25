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
import numpy as np
import matplotlib.gridspec as gridspec

plt.figure()
# 定义从-pi到pi之间的数据，平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①

# 将绘图区域分成2行3列
gs = gridspec.GridSpec(2, 3)
# 指定ax1占用第一行（0）整行
ax1 = plt.subplot(gs[0, :])
# 指定ax1占用第二行（1）的第一格（第二个参数0代表）
ax2 = plt.subplot(gs[1, 0])
# 指定ax1占用第二行（1）的第二、三格（第二个参数0代表）
ax3 = plt.subplot(gs[1, 1:3])

# 绘制正弦曲线
ax1.plot(x_data, np.sin(x_data))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.set_title('正弦曲线')

# 绘制余弦曲线
ax2.plot(x_data, np.cos(x_data))
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
ax2.set_title('余弦曲线')

# 绘制正切曲线
ax3.plot(x_data, np.tan(x_data))
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
ax3.set_title('正切曲线')

plt.show()