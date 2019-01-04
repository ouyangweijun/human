#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-01-02 19:32
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : 04-多进程实现http服务器.py
# @Desc     : 多进程实现http服务器

import socket
import re
import multiprocessing

def server_client(new_socket):
    """为这个客户端实现数据处理且返回数据"""
    # 1.接收浏览器发过来的请求，即http请求
    # GET / HTTP/1.1
    #


    request = new_socket.recv(1024).decode("utf-8")
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
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        # 2.2准备发送给浏览器的数据---boy
        # response += "<h1>hello world</h1>"
        # 将response header 发送给浏览器
        new_socket.send(response.encode("utf-8"))
        # 将response body 发送给浏览器
        new_socket.send(html_content)


    # 关闭套接字
    new_socket.close()

def main():
    """完成整体的控制"""

    # 1.创建套接字
    tcp_server_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 重复使用sock 地址

    # 2.绑定
    tcp_server_socket.bind(('127.0.0.1',8080))

    # 3.变成套接字监听
    tcp_server_socket.listen(128)


    while True:
        # 4.等待新客户端介入
        new_socket, client_addr = tcp_server_socket.accept()


        # 5.为这个客户服务
        p = multiprocessing.Process(target=server_client,args=(new_socket,))
        p.start()
        new_socket.close()
        #new_socket.close()  # 使用多线程的时候，使用的是同一个文件描述符号,因此当主线程吧资源和子线程共享的是时候，指向同一个文件描述符，所有主进程需要关闭当前这个这个指向



    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()