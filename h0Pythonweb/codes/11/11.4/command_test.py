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
import random

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.label = Label(self.master, width=30)
        self.label['font'] = ('Courier', 20)
        self.label['bg'] = 'white'
        self.label.pack()
        bn = Button(self.master, text='单击我', command=self.change)
        bn.pack()
    # 定义事件处理方法
    def change(self):
        self.label['text'] = '欢迎学习Python'
        # 生成3个随机数
        ct = [random.randrange(256) for x in range(3)]
        grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
        # 将元组中3个随机数格式化成16进制数,转成颜色格式
        bg_color = "#%02x%02x%02x" % tuple(ct)
        self.label['bg'] = bg_color
        self.label['fg'] = 'black' if grayness > 125 else 'white'
root = Tk()
root.title("简单事件处理")
App(root)
root.mainloop()
