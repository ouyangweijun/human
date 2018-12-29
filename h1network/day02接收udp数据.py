#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:oulen

"""
demo recevied upd

"""

import socket

def main():
    #1.创建一个套接字
    upd_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2.把绑定一个套接字
    localaddr=("",7788)
    upd_socket.bind(localaddr)  # 必须绑定自己的IP以及Port,其他的不行

    while True:

        #3.接收一个本地信息
        recv_data=upd_socket.recvfrom(1024)
        recv_msg = recv_data[0]  # 存储接收的数据
        send_addr = recv_data[1]  # 存储发送方的地址

        #4.打印接收到的数据
        #接收到的数据是一个元组（接收到的数据：（发送方的IP，port））
        #如果是win 使用GBK，如果是linux 使用utf-8
        print('%s:%s'%(str(send_addr),recv_msg.decode("gbk")))
    """
    C:\Python372\python.exe
    D: / human / h1network / day02接收udp数据.py
    ('192.168.245.1', 8080): 我是欧阳

    """

    #5.关闭套接字
    upd_socket.close()



if __name__ == '__main__':
    main()