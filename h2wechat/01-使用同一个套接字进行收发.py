# -*- coding:utf-8 -*-
# Author:oulen

"""
demo socket

"""

import socket

def main():

    #创建一个套接字
    upd_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    upd_socket.bind(('',4561))
    #获取对方的IP、port

    #dest_IP=input('输入对方的IP：')
    #dest_PORT=int(input('输入对方的端口：'))
    dest_IP='127.0.0.1'
    dest_PORT=4561

    #从键盘获取数据
    send_data=input("输入想要发送的数据：")

   #使用套接字接收发数据
    upd_socket.sendto(send_data.encode('gbk'),(dest_IP,dest_PORT))

    recv_data=upd_socket.recvfrom(1024)
    recv_data = upd_socket.recvfrom(1024)
    recv_msg = recv_data[0]  # 存储接收的数据
    send_addr = recv_data[1]  # 存储发送方的地址
    print('%s:%s' % (str(send_addr), recv_msg.decode("gbk")))

    # #绑定端口进行发送
    # #upd_socket.bind(("",2525))
    # while True:
    #     #从键盘获取套接字
    #     send_data=input("输入想输入的输入的数据：")
    #
    #     #输入判断为exit 就退出当前的
    #     if send_data == "exit":
    #         break
    #
    #     #可以使用一个套接字
    #     #upd_socket.sendto(b'hello world',('192.168.245.1',8080))
    #
    #     #r如果是win 使用GBK，如果是linux 使用utf-8
    #     upd_socket.sendto(send_data.encode('GBK'),('192.168.245.1',8080))

    #关闭套接字
    upd_socket.close()
if __name__ == '__main__':
    main()