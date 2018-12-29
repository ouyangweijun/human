#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:oulen

"""
demo socket

"""

import socket

def main():
    #print("aa")
    #创建一个套接字
    upd_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #可以使用一个套接字
    upd_socket.sendto(b'hello world',('192.168.245.1',8080))
    #关闭套接字
    upd_socket.close()
    print('aa')
if __name__ == '__main__':
    main()