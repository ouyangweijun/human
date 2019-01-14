#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-10 21:50
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : base_modle.py
# @Desc     : 模板类

from django.db import models

class BaseModel(models.Model):
    """模型抽象基类"""
    create_time  = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True,verbose_name="更新时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除标记")

    class Meta:
        # 说明是一个抽象模型类
        abstract = True
