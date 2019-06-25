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
import os

def files_generator():
    for filename in os.listdir(r'.'):
        yield filename

if __name__ == '__main__':
    fg = files_generator()
    print(next(fg)) # 8.1.py，生成器“冻结”在yield处
    print(next(fg)) # 8.2.py，生成器再次“冻结”在yield处
    for ele in fg:
        print(ele, end=' ')
