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
def factorial_generator(n):
    rvt_list = [1]
    for i in range(2, n + 1):
        rvt_list.append(rvt_list[-1] * i)
    print('------------', len(rvt_list))
    for i in range(n):
        yield rvt_list[i]

if __name__ == '__main__':
    fg = factorial_generator(10)
    print(next(fg)) # 1，生成器“冻结”在yield处
    print(next(fg)) # 2，生成器再次“冻结”在yield处
    for ele in fg:
        print(ele, end=' ')
