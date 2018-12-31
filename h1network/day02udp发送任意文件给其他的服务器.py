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
    #绑定端口进行发送
    upd_socket.bind(("",2525))
    while True:
        #从键盘获取套接字
        send_data=input("输入想输入的输入的数据：")

        #输入判断为exit 就退出当前的
        if send_data == "exit":
            break

        #可以使用一个套接字
        #upd_socket.sendto(b'hello world',('192.168.245.1',8080))

        #r如果是win 使用GBK，如果是linux 使用utf-8
        upd_socket.sendto(send_data.encode('GBK'),('192.168.245.1',8080))

    #关闭套接字
    upd_socket.close()
if __name__ == '__main__':
    main()