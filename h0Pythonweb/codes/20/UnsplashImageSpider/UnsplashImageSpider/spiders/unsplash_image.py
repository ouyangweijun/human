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
import scrapy, json
from UnsplashImageSpider.items import ImageItem

class UnsplashImageSpider(scrapy.Spider):
    # 定义Spider的名称
    name = 'unsplash_image'
    allowed_domains = ['unsplash.com']
    # 定义起始页面
    start_urls = ['https://unsplash.com/napi/photos?page=1&per_page=12&order_by=latest']
    def __init__ (self):
        self.page_index = 1
    
    def parse(self, response):
        # 解析服务器响应的JSON字符串
        photo_list = json.loads(response.text) # ①
        # 遍历每张图片
        for photo in photo_list:
            item = ImageItem()
            item['image_id'] = photo['id']
            item['download'] = photo['links']['download']
            yield item

        self.page_index += 1
        # 获取下一页的链接
        next_link = 'https://unsplash.com/napi/photos?page='\
            + str(self.page_index) + '&per_page=12&order_by=latest'
        # 继续获取下一页的图片
        yield scrapy.Request(next_link, callback=self.parse)
