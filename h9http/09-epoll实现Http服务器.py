#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-02 22:41
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 09-epoll实现Http服务器.py
# @Desc     : epoll实现Http服务器


import socket
import re
from select import *
import select


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

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听tcp的套接字对应的fd(文件描述符) 注册到epoll中
    epl.register(tcp_server_socket.fileno(),select.EPOLLIN)
    fd_event_dict = ()

    while True:

        fd_event_list = epl.poll()  # 默认会堵塞，之道os检测到数据 通过事件通知方式 告诉这个程序，此时才会解堵塞
        # [(fd,event),(套接字对应的文件描述符，这个文件描述符到底是什么事件， 例如可以调用recv接收等)]
        for fd ,event in fd_event_dict:
            # 等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket,client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(),select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                    server_client(fd_event_dict[fd],recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()