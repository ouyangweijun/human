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
from tkinter import *
# 导入ttk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建一个位图
        bm = PhotoImage(file = 'images/serial.png')
        # 创建一个Label，同时指定text和image
        self.label = ttk.Label(self.master, text='疯狂体\n系图书',\
            image=bm, font=('StSong', 20, 'bold'), foreground='red' )
        self.label.bm = bm
        # 设置Label默认的compound为None
        self.label['compound'] = None
        self.label.pack()
        # 创建Frame容器，用于装多个Radiobutton
        f = ttk.Frame(self.master)
        f.pack(fill=BOTH, expand=YES)
        compounds = ('None', "LEFT", "RIGHT", "TOP", "BOTTOM", "CENTER")
        # 定义一个StringVar变量，用作绑定Radiobutton的变量
        self.var = StringVar()
        self.var.set('None')
        # 使用循环创建多个Radionbutton组件
        for val in compounds:
            rb = Radiobutton(f, 
                text = val,
                padx = 20,
                variable = self.var,
                command = self.change_compound,
                value = val).pack(side=LEFT, anchor=CENTER)
    # 实现change_compound方法，用于动态改变Label的compound选项
    def change_compound(self):
        self.label['compound'] = self.var.get().lower()
root = Tk()
root.title("compound测试")
App(root)
root.mainloop()