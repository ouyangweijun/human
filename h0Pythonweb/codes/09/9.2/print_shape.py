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
'''
简单的模块，该模块包含以下内容
my_list：保存列表的变量
print_triangle: 使用星号打印三角形的函数
'''
my_list = ['Python', 'Kotlin', 'Swift']
def print_triangle(n):
    '''使用星号打印一个三角形'''
    if n <= 0:
        raise ValueError('n必须大于0')
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*' * (2 * i + 1), end='')
        print('')

# ====以下是测试代码====
def test_print_triangle():
    print_triangle(3)
    print_triangle(4)
    print_triangle(7)
if __name__ == '__main__': test_print_triangle()
