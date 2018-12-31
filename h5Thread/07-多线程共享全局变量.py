# -*- coding:utf-8 -*-
# Author:oulen

"""
多线程共享全局变量
"""

import time
import threading

g_num=100

def test1():
    global g_num
    g_num+=1
    print("----in test1 g_num=%d----" % g_num)
def test2():
    print("----in test2 g_num=%d----" % g_num)


def main():
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(2)

    print("----in main g_num=%d----" % g_num)

if __name__ == '__main__':
    main()
