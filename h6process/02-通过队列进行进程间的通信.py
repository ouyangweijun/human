# -*- coding:utf-8 -*-
# Author:oulen

"""
通过队列实现进程间的通信
"""

from multiprocessing import Queue
import multiprocessing



def download_from_web(q):
    """模拟下载数据"""
    data = [11, 22, 33, 44]

    #向队列中写数据
    for temp in data:
        q.put(temp)

    print('---下载的数据已经保存到队列中-----')

def analysis_data(q):
    """数据处理"""

    watting_analysis_data = list()
    # 从队列中获取数据

    while True:
        data=q.get()
        watting_analysis_data.append(data)

        if q.empty():
            break

    #模拟数据处理
    print(watting_analysis_data)


def main():
    """主程序实现"""

    # 1.创建一个队列
    q = multiprocessing.Queue()

    # 2.创建多个进程，将对刘娥的引用单做实参进行传递到里面去
    p1=multiprocessing.Process(target=download_from_web,args=(q,))
    p2=multiprocessing.Process(target=analysis_data,args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()


