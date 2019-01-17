# -*- coding: utf-8 -*-

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

import scrapy

class ZhipinspiderItem(scrapy.Item):
    # 工作名称
    title = scrapy.Field()
    # 工资
    salary = scrapy.Field()
    # 招聘公司
    company = scrapy.Field()
    # 工作详细链接
    url = scrapy.Field()
    # 工作地点
    work_addr = scrapy.Field()
    # 行业
    industry = scrapy.Field() 
    # 公司规模
    company_size = scrapy.Field() 
    # 招聘人
    recruiter = scrapy.Field() 
    # 发布时间
    publish_date = scrapy.Field() 
