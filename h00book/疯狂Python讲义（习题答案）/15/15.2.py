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
import re

with urlopen('http://www.crazyit.org/index.php') as f:
    # 按字节读取数据
    data = f.read()
    # 将字节数据恢复成字符串
    content = data.decode('utf-8')
    link_pattern = '<a\s+href=\"([a-zA-Z0-9\.:\?&=\-;/%]+)\"'
    it = re.finditer(link_pattern, content)
    for m in it:
        print(m.group(1))
