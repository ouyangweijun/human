# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
from concurrent.futures import ThreadPoolExecutor
import threading
import time, os
from pathlib import Path

class WriteUtil :
    def __init__ (self):
        self.current_thread_num = 1
        self.write_count = 0
 
    def write_num(self, value):
        # 生成文件位置
        with open(self.current_file_name() + ".txt", 'a+') as f:
            f.write(value + " ")
            print("ThreadNum=%d is executing. %c is written into file: %s.txt \n" % (self.current_thread_num, value, self.current_file_name()))
            self.write_count += 1
            self.current_thread_num = int(value)
            self.next_thread_num()
 
    def current_file_name(self):
        ''' 判断接下来要写哪个文件 '''
        tmp = self.write_count % 4
        name_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
        return name_map[tmp]
 
    def next_thread_num(self):
        if self.write_count % 4 == 0:
            if self.current_thread_num < 3:
                self.current_thread_num += 2
            else:
                self.current_thread_num = (self.current_thread_num + 2) % 4
        else:
            if self.current_thread_num == 4:
                self.current_thread_num = 1
            else:
                self.current_thread_num += 1

wu = WriteUtil()
wu.cond = threading.Condition()
# 提前删除4个文件
for c in ('A', 'B', 'C', 'D'):
    if Path(c + '.txt').exists():
        os.remove(c + '.txt')
def action(value):
    try:
        for i in range(10):
            try:
                wu.cond.acquire()
                # 保证要写入的值必须与当前线程的num相同
                while int(value) != wu.current_thread_num:
                    wu.cond.wait()
                wu.write_num(value)
                wu.cond.notify_all()
            finally:
                wu.cond.release()
    except Exception as e:
        print('异常%s' % e)

# 创建一个包含4条线程的线程池
pool = ThreadPoolExecutor(max_workers=4)
# 使用线程池启动4条线程
pool.submit(action, '1')
pool.submit(action, '2')
pool.submit(action, '3')
pool.submit(action, '4')

# 关闭线程池
pool.shutdown()
