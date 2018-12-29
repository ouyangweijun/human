# -*- coding:utf-8 -*-
# Author:oulen

"""
TCP demo
"""

import socket

def main():
    """创建TCP套接字"""

    # 1.创建套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.链接服务器
    tcp_socket.connect(("192.168.50.18",8080))
    # server_ip=input("输入链接的服务器IP：")
    # server_port=input("输入要链接的服务器Port:")
    # server_addr=(server_ip,server_port)


    # 3.提示用户输入数据
    # 4.接收数据、发送数据，
    send_data=input("输入发送的数据：")
    tcp_socket.send(send_data.encode('gbk'))


    # 5.关闭套接字
    tcp_socket.close()



if __name__ == '__main__':
    main()