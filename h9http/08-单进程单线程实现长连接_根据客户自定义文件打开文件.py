#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-02 07:59
# @Author  : henry_oulen
# @Software: PyCharm
# @File    : 02-单进程单线程实现长连接_根据客户自定义文件打开文件.py
# @Desc    ：单进程单线程实现长连接_根据客户自定义文件打开文件

import socket
import re


def server_client(new_socket,request):
    """为这个客户端实现数据处理且返回数据"""
    # 1.接收浏览器发过来的请求，即http请求
    # GET / HTTP/1.1
    #


    #request = new_socket.recv(1024).decode("utf-8")
    #print(request)

    request_lines = request.splitlines()
    print(request_lines)

    # GET /index.html HTTP/1.1

    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        #print(file_name)
        if file_name == "/":
            file_name = "/index.html"


    # 2.放回http格式的数据，给浏览器
    # 2.1 准备发送给浏览器的数据 --header
    # 2.返回http数据的，给浏览器
    try:
        f=open("./html"+file_name,'rb')
    except :
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += '\r\n'
        response +="---file not found---"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content
        response_header= "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += '\r\n'
        response = response_header.encode('utf-8') +response_body
        new_socket.send(response)
        # 2.2准备发送给浏览器的数据---boy
        # response += "<h1>hello world</h1>"
        # 将response header 发送给浏览器
        #new_socket.send(response.encode("utf-8"))
        # 将response body 发送给浏览器
        #new_socket.send(html_content)


    # 关闭套接字
    #new_socket.close()

def main():
    """完成整体的控制"""

    # 1.创建套接字
    tcp_server_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 重复使用sock 地址

    # 2.绑定
    tcp_server_socket.bind(('127.0.0.1',8080))

    # 3.变成套接字监听
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字设置为非堵塞

    client_socket_list = list()

    while True:
        # 4.等待新客户端介入
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass

        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode('utf-8')
            except Exception as ret:
                pass
            else:
                if recv_data:
                    server_client(client_socket,recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()