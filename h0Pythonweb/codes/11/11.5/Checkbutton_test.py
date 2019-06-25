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
        # 创建一个Label组件
        ttk.Label(self.master, text='选择您喜欢的人物:')\
            .pack(fill=BOTH, expand=YES)
        self.chars = []
        # 定义元组
        characters = ('孙悟空', '猪八戒','唐僧', '牛魔王')
        # 采用循环创建多个Checkbutton
        for ch in characters:
            intVar = IntVar()
            self.chars.append(intVar)
            cb = ttk.Checkbutton(self.master, 
                text = ch,
                variable = intVar, # 将Checkbutton绑定到intVar变量
                command = self.change) # 将选中事件绑定到self.change方法
            cb.pack(anchor=W)
        # 创建一个Label组件
        ttk.Label(self.master, text='选择您喜欢的图书:')\
            .pack(fill=BOTH, expand=YES)
        # --------------下面是第二组Checkbutton---------------
        self.books = []
        # 定义两个元组
        books = ('疯狂Python讲义', '疯狂Kotlin讲义','疯狂Swift讲义', '疯狂Java讲义')
        vals = ('python', 'kotlin','swift', 'java')
        i = 0
        # 采用循环创建多个Checkbutton
        for book in books:
            strVar = StringVar()
            self.books.append(strVar)
            cb = ttk.Checkbutton(self.master, 
                text = book,
                variable = strVar, # 将Checkbutton绑定到strVar变量
                onvalue = vals[i],
                offvalue = '无',
                command = self.books_change) # 将选中事件绑定到books_change方法
            cb.pack(anchor=W)
            i += 1
    def change(self):
        # 将self.chars列表转换成元素为str的列表
        new_li = [str(e.get()) for e in self.chars]
        # 将new_li列表连接成字符串
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)
    def books_change(self):
        # 将self.books列表转换成元素为str的列表
        new_li = [e.get() for e in self.books]
        # 将new_li列表连接成字符串
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)
root = Tk()
root.title("Checkbutton测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
