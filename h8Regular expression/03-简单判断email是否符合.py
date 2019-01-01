#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-02 01:05
# @Author  : henru_oulen
# @Software: PyCharm
# @File    : 03-简单判断email是否符合.py
# 功能：简单判断email是否符合

import re

def main():

    email = input("请输入一个邮箱地址：")

    # 如果在正则表达式中需要用到某些普通的符号，比如. 比如？ 等，仅仅需要在加上一个 反斜杠进行转义

    ret = re.match(r"^[a-zA-Z_0-9]{4,20}@163\.com$",email)
    if ret:
        print('%s 符合要求。。。' % email)
    else:
        print('%s不符合要求...' % email)

if __name__ == '__main__':
    main()


"""
C:\Python372\python.exe "D:/human/h8Regular expression/03-简单判断email是否符合.py"
请输入一个邮箱地址：aa@163.com
aa@163.com不符合要求...

"""