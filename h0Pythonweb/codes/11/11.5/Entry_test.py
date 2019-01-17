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
from tkinter import messagebox
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建Entry组件
        self.entry = ttk.Entry(self.master,
            width=44,
            font=('StSong', 14), 
            foreground='green')
        self.entry.pack(fill=BOTH, expand=YES)
        # 创建Entry组件
        self.text = Text(self.master,
            width=44,
            height=4,
            font=('StSong', 14), 
            foreground='gray')
        self.text.pack(fill=BOTH, expand=YES)
        # 创建Frame作为容器
        f = Frame(self.master)
        f.pack()
        # 创建五个按钮，将其放入Frame中
        ttk.Button(f, text='开始插入', command=self.insert_start).pack(side=LEFT)
        ttk.Button(f, text='编辑处插入', command=self.insert_edit).pack(side=LEFT)
        ttk.Button(f, text='结尾插入', command=self.insert_end).pack(side=LEFT)
        ttk.Button(f, text='获取Entry', command=self.get_entry).pack(side=LEFT)
        ttk.Button(f, text='获取Text', command=self.get_text).pack(side=LEFT)
    def insert_start(self):
        # 在Entry和Text开始处插入内容
        self.entry.insert(0, 'Kotlin')
        self.text.insert(1.0, 'Kotlin')
    def insert_edit(self):
        # 在Entry和Text的编辑处插入内容
        self.entry.insert(INSERT, 'Python')
        self.text.insert(INSERT, 'Python')
    def insert_end(self):
        # 在Entry和Text的结尾处插入内容
        self.entry.insert(END, 'Swift')
        self.text.insert(END, 'Swift')
    def get_entry(self):
        messagebox.showinfo(title='输入内容', message=self.entry.get())
    def get_text(self):
        messagebox.showinfo(title='输入内容', message=self.text.get(1.0, END))
root = Tk()
root.title("Entry测试")
App(root)
root.mainloop()