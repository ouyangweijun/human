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
def test(val, step):
    print("--------函数开始执行------")
    cur = 0
    # 遍历0～val
    for i in range(val):
        # cur添加i*step
        cur += i * step
        yield cur
#        print(cur, end=' ')
# 执行函数，返回生成器
t = test(10, 2)
print('=================')
# 获取生成器的第一个值
print(next(t)) # 0，生成器“冻结”在yield处
print(next(t)) # 2，生成器再次“冻结”在yield处

for ele in t:
    print(ele, end=' ')

# 再次创建生成器
t = test(10, 1)
# 将生成器转换成列表
print(list(t))
# 再次创建生成器
t = test(10, 3)
# 将生成器转换成列表
print(tuple(t))