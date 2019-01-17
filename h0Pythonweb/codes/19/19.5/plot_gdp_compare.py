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
import json
from matplotlib import pyplot as plt
import numpy as np

filename = 'gdp_json.json'
# 读取JSON格式的GDP数据
with open(filename) as f:
    gpd_list = json.load(f)
# 使用list列表依次保存中国、美国、日本、俄罗斯、加拿大的GDP值
country_gdps = [{}, {}, {}, {}, {}]
country_codes = ['CHN', 'USA', 'JPN', 'RUS', 'CAN']
# 遍历列表的每个元素，每个元素是一个GDP数据项
for gpd_dict in gpd_list:
    for i, country_code in enumerate(country_codes):
        # 只读取指定国家的数据
        if gpd_dict['Country Code'] == country_code:
            year = gpd_dict['Year']
            # 只读取2001年到2016
            if 2017 > year > 2000:
                country_gdps[i][year] = gpd_dict['Value']
# 使用list列表依次保存中国、美国、日本、俄罗斯、加拿大的GDP值
country_gdp_list = [[], [], [], [], []]
# 构建时间数据
x_data = range(2001, 2017)
for i in range(len(country_gdp_list)):
    for year in x_data:
        # 除以1e8，让数值变成以亿为单位
        country_gdp_list[i].append(country_gdps[i][year] / 1e8)
bar_width=0.15
fig = plt.figure(dpi=128, figsize=(15, 8))
colors = ['indianred', 'steelblue', 'gold', 'lightpink', 'seagreen']
# 定义国家名称列表
countries = ['中国', '美国', '日本', '俄罗斯', '加拿大']
# 采用循环绘制5组柱状图
for i in range(len(colors)):
    # 使用自定义X坐标将数据分开
    plt.bar(x=np.arange(len(x_data))+bar_width*i, height=country_gdp_list[i],
        label=countries[i], color=colors[i], alpha=0.8, width=bar_width)
    # 仅为中国、美国的条柱上绘制GDP数值
    if i < 2:
        for x, y in enumerate(country_gdp_list[i]):
            plt.text(x, y + 100, '%.0f' % y, ha='center', va='bottom')
# 为X轴设置刻度值
plt.xticks(np.arange(len(x_data))+bar_width*2, x_data)
# 设置标题
plt.title("2001到2016年各国GDP对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("GDP(亿美元)")
# 显示图例
plt.legend()
plt.show()
