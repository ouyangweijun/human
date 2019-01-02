#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-02 07:59
# @Author  : henry_oulen
# @Software: PyCharm
# @File    : 02-实现简单的http服务器.py
# 功能：实现简单的http服务器

import socket


def server_client(new_socket):
    """为这个客户端实现数据处理且返回数据"""
    # 1.接收浏览器发过来的请求，即http请求
    # GET / HTTP/1.1
    #
    request = new_socket.recv(1024)
    print(request)

    # 2.放回http格式的数据，给浏览器
    # 2.1 准备发送给浏览器的数据 --header

    response = "HTTP/1.1 200 OK\r\n"
    response += '\r\n'
    # 2.2准备发送给浏览器的数据---boy
    response += "<h1>hello world</h1>"
    new_socket.send(response.encode("utf-8"))

    # 关闭套接字
    new_socket.close()

def main():
    """完成整体的控制"""

    # 1.创建套接字
    tcp_server_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定
    tcp_server_socket.bind(('127.0.0.1',8080))

    # 3.变成套接字监听
    tcp_server_socket.listen(128)

    while True:
        # 4.等待新客户端介入
        new_socket, client_addr = tcp_server_socket.accept()

        # 5.为这个客户服务
        server_client(new_socket)


    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()