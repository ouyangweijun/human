#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 23:46
# @Author  : henru_oulen
# @File    : 01-regluar.py
# 功能：正则表达式

import re

# re.match('正则表达式','需要处理的数据')

"""
匹配单个字符
在上一小节中，了解到通过re模块能够完成使用正则表达式来匹配字符串

本小节，将要讲解正则表达式的单字符匹配

字符	功能
.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配单词字符，即a-z、A-Z、0-9、_
\W	匹配非单词字符

"""



"""
匹配多个字符
匹配多个字符的相关格式

字符	功能
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次


"""

print(re.match(r'[hh]ello','hello world'))  # 判断大小写
print(re.match(r'hello\d+','hello65 world'))  # 判断数字
print(re.match(r'hello\d+','hello65 world').group())  # 判读数子贪婪模式
print(re.match(r'hello[1-9]+','hello65 world').group())  # 判断数字范围
print(re.match(r'hello[12935]+','hello6 world').group())  # 判断数字范围
print(re.match(r'hello[1-5abc]+','helloa world').group())  # 判断字母范围
print(re.match(r'hello[1-5a-zA-Z]+','helloa world').group())  # 判断大小写
print(re.match(r'hello\w','helloa world').group())  # 出去特殊符号
