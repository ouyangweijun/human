# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
# Python 2.x使用这行
#from Tkinter import *
# Python 3.x使用这行
from tkinter import *  

# 创建窗口并设置窗口标题
root = Tk()
# 设置窗口标题
root.title('Pack布局')
for i in range(3):
    lab = Label(root, text="第%d个Label" % (i + 1), bg='#eeeeee')
    # 调用pack进行布局
    lab.pack()
# 启动主窗口的消息循环
root.mainloop()