#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-04 09:06
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 03-JDselect_mysql.py
# @Desc     :

from pymysql import connect

class JD(object):
    """创建一个用户查询类"""

    def __init__(self):
        pass

    def run(self):
        pass
        while True:
            print("-----京东-----")
            print("1:查询全部的商品")
            print("2:所有的商品分类")
            print("3:所有的商品品牌分类")
            num = input("请输入功能对应的序号：")

            if num == 1:
                #查询所有商品
                self.show_all_items()


def main():
    """主要的控制实现"""

if __name__ == '__main__':
    main()