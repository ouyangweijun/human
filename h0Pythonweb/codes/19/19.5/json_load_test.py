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

filename = 'gdp_json.json'

with open(filename) as f:
    gpd_list = json.load(f)
# 遍历列表的每个元素，每个元素是一个GDP数据项
for gpd_dict in gpd_list:
    # 只显示中国、2016年的GDP
    if gpd_dict['Year'] == 2016 and gpd_dict['Country Code'] == 'CHN':
        print(gpd_dict['Country Name'], gpd_dict['Value'])