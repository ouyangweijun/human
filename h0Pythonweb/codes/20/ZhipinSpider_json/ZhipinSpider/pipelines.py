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
import json

class ZhipinspiderPipeline(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        self.json_file = open("job_positions.json", "wb+")
        self.json_file.write('[\n'.encode("utf-8"))
    # 重写close_spider回调方法，用于关闭文件
    def close_spider(self, spider):
        print('----------关闭文件-----------')
        # 后退2个字符，也就是去掉最后一条记录之后的换行符和逗号
        self.json_file.seek(-2, 1)
        self.json_file.write('\n]'.encode("utf-8"))
        self.json_file.close()
    def process_item(self, item, spider):
        # 将item转换成JSON字符串
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # 写入JSON字符串
        self.json_file.write(text.encode("utf-8"))