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
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count
my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
# 获取sum_and_avg函数返回的多个值，多个返回值被封装成元组
tp = sum_and_avg(my_list) #①
print(tp)
# 使用序列解包来获取多个返回值
s, avg = sum_and_avg(my_list) #②
print(s)
print(avg)