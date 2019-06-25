#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-05-30 08:18
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : config.py
# @Desc     :

import os

BASE_DIRS=os.path.dirname(__file__)

options={
    'port':8080,
    'list':['good','nice','hangdsome']
}


# 配置

settings={
    'static_path':os.path.join(BASE_DIRS,'static'),
    'template_path': os.path.join(BASE_DIRS, 'templates'),

    'debug':True,
    'autoreload':True
}