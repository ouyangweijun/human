#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-02 01:21
# @Author  : henru_oulen
# @Software: PyCharm
# @File    : 04-正则的高级应用.py
# 功能：04-正则的高级应用2


"""
re模块的高级用法
search
需求：匹配出文章阅读的次数
"""
#coding=utf-8
import re

ret = re.search(r"\d+", "阅读次数为 9999")
ret.group()
# 运行结果：
#
# '9999'



# findall
# 需求：统计出python、c、c++相应文章阅读的次数

#coding=utf-8
import re

ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)
# 运行结果：
#
# ['9999', '7890', '12345']


# sub 将匹配到的数据进行替换
# 需求：将匹配到的阅读次数加1
#
# 方法1：

#coding=utf-8
import re

ret = re.sub(r"\d+", '998', "python = 997")
print(ret)
# 运行结果：
#
# python = 998


# 方法2：

#coding=utf-8
import re

def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret = re.sub(r"\d+", add, "python = 997")
print(ret)

ret = re.sub(r"\d+", add, "python = 99")
print(ret)
# 运行结果：
#
# python = 998
# python = 100


