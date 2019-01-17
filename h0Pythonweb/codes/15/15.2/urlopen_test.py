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
from urllib.request import *

# 打开URL对应的资源
result = urlopen('http://www.crazyit.org/index.php')
# 按字节读取数据
data = result.read(326)
# 将字节数据恢复成字符串
print(data.decode('utf-8'))

# 用context manager来管理打开的URL资源
with urlopen('http://www.crazyit.org/index.php') as f:
    # 按字节读取数据
    data = f.read(326)
    # 将字节数据恢复成字符串
    print(data.decode('utf-8'))
