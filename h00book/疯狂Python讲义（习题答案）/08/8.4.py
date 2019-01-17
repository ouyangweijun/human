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
def card_generator():
    nums = 52
    flowers = ('♠', '♥', '♣', '♦')
    values = ('2', '3', '4', '5',
        '6', '7', '8', '9',
        '10', 'J', 'Q', 'K', 'A')
    for i in range(nums):
        yield flowers[i // 13] + values[i % 13]

if __name__ == '__main__':
    cg = card_generator()
    print(next(cg)) # ♠2，生成器“冻结”在yield处
    print(next(cg)) # ♠3，生成器再次“冻结”在yield处
    for ele in cg:
        print(ele, end=' ')
