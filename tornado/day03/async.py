#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-19 07:16
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : sync.py
# @Desc     :

import time
import threading


def finsh(data):
    print('开始处理回调函数')
    print('收到longIO的相应数据，',data)
    print('结束处理回调函数')




def reA():
    print('开始 处理A')
    res = longIo(finsh)
    print('结束 处A')


def reB():
    print('开始 处理B')
    time.sleep(1)
    print('结束 处B')

def longIo(callback):
    def run(cb):
        print('开始 耗时')
        time.sleep(5)
        print('结束 耗时')
        cb('sun is a good man')
    threading.Thread(target=run,args=(callback,)).start()




def main():
    reA()
    reB()
    while 1:
        time.sleep(1)
        pass
if __name__ == '__main__':
    main()
