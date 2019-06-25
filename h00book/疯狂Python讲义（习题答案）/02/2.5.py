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
string, sub_string = input("请输入字符串:"), input("请输入子串:")
# 字符串长度
str_len = len(string)
# 子串长度
sub_str_len = len(sub_string)
ct = 0  
for i in range(str_len-1): 
    # 每次取和子字符串长度相等的字符串和子字符串进行比较
    if string[i:i + sub_str_len] == sub_string: 
        ct += 1
print("子串在字符串中出现的次数：%d" % ct)
