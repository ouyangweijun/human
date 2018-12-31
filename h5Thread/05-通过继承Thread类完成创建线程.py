# -*- coding:utf-8 -*-
# Author:oulen

"""
没有多线程
"""

import time
import threading


def sing():
    """唱歌5秒"""
    print(threading.enumerate())
    for i in range(5):
        print("正在唱歌%d" % i)
        time.sleep(1)

def dance():
    """跳舞5秒"""
    print(threading.enumerate())
    for i in range(5):
        print("正在跳舞%d" %i)
        time.sleep(1)

def main():


    t1=threading.Thread(target=sing)
    print(threading.enumerate())
    t2=threading.Thread(target=dance)
    print(threading.enumerate())
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=1:
            break
        time.sleep(1)
class MyTread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg="I am" +self.name+"@"+str(i)  # name 属性中保存的是当前线程的名字
            self.login()
            self.register()
            print(msg)
    def login(self):
        print('这是登陆代码')
    def register(self):
        print("这是注册代码")

if __name__ == '__main__':
    #main()
    t=MyTread()
    t.start()
# 1.主线程等待子线程结束
# 2.子线程结束是从子函数结束停止， 子线程开始是在start的时候进行创建


"""
C:\Python372\python.exe D:/human/h5Thread/03-查看线程数量.py
正在唱歌0
正在跳舞0[<_MainThread(MainThread, started 34492)>, <Thread(Thread-1, started 32800)>, <Thread(Thread-2, started 29320)>]

[<_MainThread(MainThread, started 34492)>, <Thread(Thread-1, started 32800)>, <Thread(Thread-2, started 29320)>]
正在唱歌1正在跳舞1

[<_MainThread(MainThread, started 34492)>, <Thread(Thread-1, started 32800)>, <Thread(Thread-2, started 29320)>]正在唱歌2
正在跳舞2

[<_MainThread(MainThread, started 34492)>, <Thread(Thread-1, started 32800)>, <Thread(Thread-2, started 29320)>]
正在唱歌3
正在跳舞3
[<_MainThread(MainThread, started 34492)>, <Thread(Thread-1, started 32800)>, <Thread(Thread-2, started 29320)>]
正在跳舞4
正在唱歌4
[<_MainThread(MainThread, started 34492)>, <Thread(Thread-1, started 32800)>, <Thread(Thread-2, started 29320)>]
[<_MainThread(MainThread, started 34492)>]

Process finished with exit code 0

"""


"""
I amThread-1@0
I amThread-1@1
I amThread-1@2
I amThread-1@3
I amThread-1@4
"""