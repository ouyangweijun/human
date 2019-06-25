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
a_list = [330, 1.4, 50, 'fkit', -3.5]
# 遍历0到len(a_list)的范围
for i in range(0, len(a_list)) :
    # 根据索引访问列表元素
    print("第%d个元素是 %s" % (i , a_list[i]))
    