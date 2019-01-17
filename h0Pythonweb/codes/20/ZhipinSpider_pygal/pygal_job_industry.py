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
import pygal, codecs

filename = 'job_positions.json'
# 读取JSON格式的工作数据
with codecs.open(filename, 'r', 'utf-8', buffering=True) as f:
    job_list = json.load(f)
# 定义job_dict来保存各行业的招聘职位数
job_dict = {}
# 遍历列表的每个元素，每个元素是一个招聘信息
for job in job_list:
    if job['industry'] in job_dict:
        job_dict[job['industry']] += 1
    else:
        job_dict[job['industry']] = 1

# 创建pygal.Pie对象（饼图）
pie = pygal.Pie()
other_num = 0
# 采用循环为饼图添加数据
for k in job_dict.keys():
    # 如果该行业的招聘职位少于5，统一归为“其他”
    if job_dict[k] < 5:
        other_num += job_dict[k]
    else:
        pie.add(k, job_dict[k])
# 添加其他行业的招聘职位数
pie.add('其他', other_num)
pie.title = '广州地区各行业热门招聘统计图'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
pie.render_to_file('job_position.svg')
