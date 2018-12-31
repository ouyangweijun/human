# -*- coding:utf-8 -*-
# Author:oulen

"""
多线程UDP 聊天
"""

import socket
import time
import threading

def recv_msg(udp_socket):
    """接收数据"""

    # 接收数据
    while True:
        recv_data=udp_socket.recvfrom(1024)
        print(recv_data.decode('gbk'))

def send_msg(udp_socket,dest_ip,dest_port):
    """发送数据"""


    # 发送数据
    while True:
        send_data=input("输入想要发送的数据：")
        udp_socket.sendto(send_data.encode('gbk'),(str(dest_ip),int(dest_port)))


def main():
    """完成udp聊天器的整体控制"""

    # 1.创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2.绑定本地信息
    udp_socket.bind(("192.168.50.18",7890))

    # 3.获取对方的IP
    dest_ip='192.168.50.18'
    dest_port=7781

    # 4.创建2个子线程进行执行对应的功能
    t_recv=threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send=threading.Thread(target=send_msg, args=(udp_socket,dest_ip,dest_port))

    t_recv.start()
    t_send.start()



if __name__ == '__main__':
    main()