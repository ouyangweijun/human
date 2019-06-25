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
src_list = [12, 45, 3.4, 12, 'fkit', 45, 3.4, 'fkit', 45, 3.4]
statistics = {}
for ele in src_list:
    # 如果字典中包含ele代表的key
    if ele in statistics:
        # 将ele元素代表出现次数加1
        statistics[ele] += 1
    # 如果字典中不包含ele代表的key，说明该元素还未出现国
    else:
        # 将ele元素代表出现次数设为1
        statistics[ele] = 1        
# 遍历dict，打印出各元素的出现次数
for ele, count in statistics.items():
    print("%s的出现次数为:%d" % (ele, count))
    