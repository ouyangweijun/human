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
# 导入访问MySQL的模块
import mysql.connector

class ZhipinspiderPipeline(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='32147',
            host='localhost', port='3306',
            database='python', use_unicode=True)
        self.cur = self.conn.cursor()
    # 重写close_spider回调方法，用于关闭数据库资源
    def close_spider(self, spider):
        print('----------关闭数据库资源-----------')
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()
    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO job_inf VALUES(null, %s, %s, %s, %s, %s, \
            %s, %s, %s, %s)", (item['title'], item['salary'], item['company'],
            item['url'], item['work_addr'], item['industry'], 
            item.get('company_size'), item['recruiter'], item['publish_date']))
        self.conn.commit()