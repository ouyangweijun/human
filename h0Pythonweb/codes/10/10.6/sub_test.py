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
import re
my_date = '2008-08-18'
# 将my_date字符串里中画线替换成斜线
print(re.sub(r'-', '/' , my_date))
# 将my_date字符串里中画线替换成斜线，只替换一次
print(re.sub(r'-', '/' , my_date, 1))

# 在匹配的字符串前后添加内容
def fun(matched):
    # matched就是匹配对象，通过该对象的group()方法可获取被匹配的字符串
    value = "《疯狂" + (matched.group('lang')) + "讲义》"
    return value
s = 'Python很好，Kotlin也很好'
# 将s里面的英文单词（用re.A旗标控制）进行替换
# 使用fun函数指定替换的内容
print(re.sub(r'(?P<lang>\w+)', fun, s, flags=re.A))