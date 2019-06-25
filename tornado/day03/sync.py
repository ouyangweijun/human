#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-19 07:16
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : sync.py
# @Desc     :

import time


def reA():
    print('开始 处理A')
    print('结束 处A')


def reB():
    print('开始 处理B')
    print('结束 处B')

def longIo():
    time.sleep(5)



def main():
    reA()
    reB()
    while 1:
        time.sleep(1)
        pass
if __name__ == '__main__':
    main()
