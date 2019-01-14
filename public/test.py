#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-14 21:32
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : test.py
# @Desc     :

c=[ str(x)+"*"+str(y)+"="+str(x*y) for x in range(1,10) for y in range(1,10)]
print(c)