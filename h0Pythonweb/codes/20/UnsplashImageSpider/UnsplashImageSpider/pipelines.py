# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

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

class UnsplashimagespiderPipeline(object):
    def process_item(self, item, spider):
        # 每个item代表一个要下载的图片
        print('----------' + item['image_id'])
        real_url = item['download'] + "?force=true"
        try:
            pass
            # 打开URL对应的资源
            with urlopen(real_url) as result:
                # 读取图片数据
                data = result.read()
                # 打开图片文件
                with open("images/" + item['image_id'] + '.jpg', 'wb+') as f:
                    # 写入读取的数据
                    f.write(data)
        except:
            print('下载图片出现错误' % item['image_id'])
