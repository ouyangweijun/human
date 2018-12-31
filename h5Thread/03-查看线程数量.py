# -*- coding:utf-8 -*-
# Author:oulen

"""
没有多线程
"""

import time
import threading


def sing():
    """唱歌5秒"""
    for i in range(5):
        print("正在唱歌%d" % i)
        time.sleep(1)

def dance():
    """跳舞5秒"""
    for i in range(5):
        print("正在跳舞%d" %i)
        time.sleep(1)

def main():


    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=1:
            break
        time.sleep(1)

if __name__ == '__main__':
    main()

# 1.主线程等待子线程结束
# 2.子线程结束是从子函数结束停止，子线程开始是在start的时候进行创建