# -*- coding:utf-8 -*-
# Author:oulen

"""
进程池概述
"""

from multiprocessing import Pool

import os ,time,random

def work(msg):
    t_start=time.time()
    print("%s开始执行，进程号是%d " % (msg,os.getpgid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))

po = Pool(3)
for i in range(0, 10):
    # Pool().apply_async (需要调用 的目标，传递给目标参数元组，)
    # 每次循环将会调用空闲的子进程去调用目标
    po.apply_async(work, (i,))
print('----staart----')
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中全部子进程执行完成，必须放在close语句以后
print("--=end =---")

# linux 版本