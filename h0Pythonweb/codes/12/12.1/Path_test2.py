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
from pathlib import *

p = Path('a_test.txt')
# 以GBK字符集输出文本内容
result = p.write_text('''有一个美丽的新世界
它在远方等我
那里有天真的孩子
还有姑娘的酒窝''',  encoding='GBK')
# 返回输出的字符数
print(result)

# 指定以GBK字符集读取文本内容
content = p.read_text(encoding='GBK')
# 输出读取的文本内容
print(content)

# 读取字节内容
bb = p.read_bytes()
print(bb)