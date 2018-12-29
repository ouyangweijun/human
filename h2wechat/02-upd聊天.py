# -*- coding:utf-8 -*-
# Author:oulen

"""
UDP 聊天
"""

import socket

def send_msg(udp_socket):
    """发送消息"""
    # 获取发送的内容
    dest_ip = input("输入对方的信息IP：")
    dest_port = int(input('输入对方的端口：'))
    send_data = input("输入想要发送的信息：")
    udp_socket.sendto(send_data.encode("GBK"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data=udp_socket.recvfrom(1024)
    recv_msg = recv_data[0]  # 存储接收的数据
    send_addr = recv_data[1]  # 存储发送方的地址
    print('%s:%s' % (str(send_addr), recv_msg.decode("gbk")))


def main():
    # 创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定套接字
    udp_socket.bind(("",7788))

    # 循环来处理事情
    while True:
        # 发送
        send_msg(udp_socket)



        # 接收并且显示

        recv_msg(udp_socket)


if __name__ == '__main__':
    main()

