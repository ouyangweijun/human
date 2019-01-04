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

    def show_all_items(self):
        """现实全部的商品"""

        sql = "select * from goods;"
        cursor.execute(sql)
        for temp in cursor.fetchall():
            print(temp)

    def run(self):
        pass
        while True:
            print("-----京东-----")
            print("1:查询全部的商品")
            print("2:所有的商品分类")
            print("3:所有的商品品牌分类")
            num = input("请输入功能对应的序号：")

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