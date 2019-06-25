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
a_list = [3, 4, -2, -30, 14, 9.3, 3.4]
# 对列表元素排序
a_list.sort()
print(a_list) #[-30, -2, 3, 3.4, 4, 9.3, 14]
b_list = ['Python', 'Swift', 'Ruby', 'Go', 'Kotlin', 'Erlang']
# 对列表元素排序：默认按字符串包含的字符的编码大小比较
b_list.sort()
print(b_list) # ['Erlang', 'Go', 'Kotlin', 'Python', 'Ruby', 'Swift']

# 指定key为len，指定使用len函数对集合元素生成比较的键，
# 也就是按字符串的长度比较大小
b_list.sort(key=len)
print(b_list) # ['Go', 'Ruby', 'Swift', 'Erlang', 'Kotlin', 'Python']
# 指定反向排序
b_list.sort(key=len, reverse=True)
print(b_list) # ['Erlang', 'Kotlin', 'Python', 'Swift', 'Ruby', 'Go']


# 以下代码只能在Python 2.x中执行
# 定义一个根据长度比较大小的比较函数
def len_cmp(x, y):
    # 下面代码比较大小的逻辑是：长度大的字符串就算更大
    return 1 if len(x) > len(y) else (-1 if len(x) < len(y) else 0)
b_list.sort(len_cmp)
print(b_list) #['Go', 'Ruby', 'Swift', 'Erlang', 'Kotlin', 'Python']