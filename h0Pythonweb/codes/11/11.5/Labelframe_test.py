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
        # 创建Labelframe容器
        lf = ttk.Labelframe(self.master, text='请选择图书',
            padding=20)
        lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        books = ['Swift', 'Python', 'Kotlin', 'Ruby']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个Radiobutton，并放入Labelframe中
        for book in books:
            Radiobutton(lf, text='疯狂' + book + '讲义',
            value=i,
            variable=self.intVar).pack(side=LEFT)
            i += 1     
root = Tk()
root.title("Labelframe测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
