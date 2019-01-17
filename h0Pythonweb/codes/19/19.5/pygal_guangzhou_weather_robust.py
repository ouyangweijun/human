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
import csv
import pygal
from datetime import datetime
from datetime import timedelta

filename = 'guangzhou-2017.csv'
# 打开文件
with open(filename) as f:
    # 创建cvs文件读取器
    reader = csv.reader(f)
    # 读取第一行，这行是表头数据。
    header_row = next(reader)
    print(header_row)

    # 准备展示的数据
    shades, sunnys, cloudys, rainys = 0, 0, 0, 0
    prev_day = datetime(2016, 12, 31)
    for row in reader:
        try:
            # 将第一列的值格式化为日期
            cur_day = datetime.strptime(row[0], '%Y-%m-%d')
            description = row[3]
        except ValueError:
            print(cur_day, '数据出现错误')
        else:
            # 计算前、后两天数据的时间差
            diff = cur_day - prev_day
            # 如果前、后两天数据的时间差不是相差一天，说明数据有问题
            if diff != timedelta(days=1):
                print('%s之前少了%d天的数据' % (cur_day, diff.days - 1))
            prev_day = cur_day   
            if '阴' in description:
                shades += 1
            elif '晴' in description:
                sunnys += 1
            elif '云' in description:
                cloudys += 1
            elif '雨' in description:
                rainys += 1
            else:
                print(description)
# 创建pygal.Pie对象（饼图）
pie = pygal.Pie()
# 为饼图添加数据
pie.add("阴", shades)
pie.add("晴", sunnys)
pie.add("多云", cloudys)
pie.add("雨", rainys)
pie.title = '2017年广州天气汇总'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
pie.render_to_file('guangzhou_weather.svg')
