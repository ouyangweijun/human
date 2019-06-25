#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-16 20:06
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : a.py
# @Desc     :

import pandas as pd
import csv
from pymongo import *


def insert():
    with open('wandoujia_app_cat_2.csv', 'r+', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    j = 1
    for i in rows:
        # print(i)
        ss='app名称,英文名称,一级分类,安装人数,软件大小,头像地址,描述,新版本截图,开发者,apk下载地址,软件短评,版本号,id号码,vcode,新版本号'
        a0 = i[0]  # app名称
        a1 = i[1]  # 英文名称
        a2 = i[2]  # 一级分类
        a3 = i[3]  # 安装人数
        a4 = i[4]  #  软件大小
        a5 = i[5]  # 头像地址
        a6 = i[6]  # 描述
        a7 = i[7]  # 新版本截图
        if a0=='天下狼烟':
            print(a0)
            pass
        try:
            print(a0)
            a7 = i[7]  # 新版本截图
        except Exception as e:
            print(a0)
            pass
        a8 = i[8]  # 开发者
        a9 = i[9]  # apk下载地址
        a10 = i[10]  # 软件短评
        a11 = i[11]  # 版本号
        # a12 = i[11]  #
        j +=1
        # a12 = i[12]
        # a13 = i[13]
        # a14 = i[14]
        print(a7)
        # if a2 =='旅游出行':
        #     print(a2)
        # a13 = a11.strip()
        # #print(a11)
        # #print(a11[-1])
        # try:
        #     ssd = int(a13[-1])
        #     # sa = int(a11[0])
        # except Exception as e:
        #     print(a13[-1],'这是-1')
        #     print(a13)
        #
        # try:
        #     # ssd = int(a11[-1])
        #     sa = int(a13[0])
        # except Exception as e:
        #     print(a13[0],'这是0')
        #     print(a13)

        #print(type(a7))
        # a100 = a7.split(',')
        # print(type(a100))
        # print(a100)

        # for jjj in a7:
        #     print(jjj)
        #     print('aaf')
        # if a11 == '未知':
        #     print(type(a11))
        # else:
        #     pass
        #print(str(a11).strip())

        # if  a3.endswith('万人安装'):
        #     #print(a3)
        #     pass
        # elif a3.endswith('亿人安装'):
        #     pass
        #     #print()
        # elif a3.endswith("人安装"):
        #     pass
        # else:
        #     print(a3)
        # if j ==10:
        #     break


        # if  not a4.endswith('MB'):
        #     print(a4)
        # elif a4.endswith('MB'):
        #     pass

        #print(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)

        # try:
        #     # 1 创建连接对象
        #     client = MongoClient(host="192.168.0.77", port=27017)
        #     # 2 获取数据库,
        #     # 如果这个数据库不存在，就在内存中虚拟创建
        #     # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        #     db = client.vstore_db  # 使用demo数据库
        #     # 向stu集合插入数据
        #     # 插入一条
        #     sjson =             {
        #             "cp": a8,
        #             "fileInfo": {
        #                 "androidAttributer": {
        #                     "packageName": a1,
        #                     "versionCode": "80960",
        #                     "versionName": a11
        #                 },
        #                 "path": a9,
        #                 "name": a8,
        #                 "size": a4,
        #                 "format": "android"
        #             },
        #             "gameRes": {
        #                 "ver": a11,
        #                 "age": 18,
        #                 "language": "中文",
        #                 "region": "中国"
        #             },
        #             "icons":
        #                 a5
        #             ,
        #             "keyword":
        #                 a2
        #             ,
        #             "previewMaps":
        #                 a7
        #             ,
        #             "productDesc":a6,
        #             "productTag": a2,
        #             "provide": a8,
        #             "sort": "Game",
        #             "star": 5,
        #             "categoryName": a8,
        #             "downloadCount": a3,
        #             "name": a0,
        #             "extComment": a10,
        #             "category": "软件"
        #         }
        #     db.subResource1.insert_one(sjson)
        # except Exception as e:
        #     print(e)

if __name__ == '__main__':
    insert()


