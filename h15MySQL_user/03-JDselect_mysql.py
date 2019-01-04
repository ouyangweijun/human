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
        # 创建链接
        self.conn = connect(host='192.168.50.69',port=3316,user='hotdb_cloud',password='hotdb_cloud',database='jing_dong',charset="utf8")
        # 活动cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示全部的商品"""
        sql = "select * from goods;"
        self.execute_sql(sql)
    def show_create(self):
        sql = 'select name from goods_cates'
        self.execute_sql(sql)

    def show_brands(self):
        sql = 'select name from goods_brands'
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("-----京东-----")
        print("1:查询全部的商品")
        print("2:所有的商品分类")
        print("3:所有的商品品牌分类")
        return input("请输入功能对应的序号：")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                #查询所有商品
                self.show_all_items()
            elif num == "2":
                # 查询分类
                pass
            elif num == "3":
                # 查询品牌分类
                pass
            else:
                print("输入有误，重新输入")



def main():
    """主要的控制实现"""

    # 创建一个京东商城对象
    jd = JD()

    # 2.调用这个对象run 方法，让他运行
    jd.run()
if __name__ == '__main__':
    main()