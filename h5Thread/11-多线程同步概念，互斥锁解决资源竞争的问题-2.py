# -*- coding:utf-8 -*-
# Author:oulen

"""
多线程共享全局变量，锁在循环里面
"""

import time
import threading

g_num=0

def test1(num):
    global g_num
    # 1.上锁，如果是之前么有被上锁，那么此时上锁成功
    # 2.如果之前已经上锁，那么此时会被堵塞这这里，直到这个锁被解开
    for i in range(num):
        mutex.acquire()
        g_num+=1
        mutex.release()
    print("----in test1 g_num=%d----" % g_num)

# 1.创建一个互斥锁,默认是没有上锁的
mutex=threading.Lock()

def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num+=1
        mutex.release()
    print("----in test2 g_num=%d----" % g_num)

g_nums=[11,33]

def main():

    # target 指定将来 这个线程去调用那个 函数执行代码
    # args 指定将来调用 函数的时候 传递什么数据过去-
    t1=threading.Thread(target=test1,args=(10000000,))  # 1.args里一定是一个元组
    t2=threading.Thread(target=test2,args=(10000000,))

    t1.start()
    t2.start()
    time.sleep(2)

    print("----in main g_num=%d----" % g_num)

if __name__ == '__main__':
    main()
