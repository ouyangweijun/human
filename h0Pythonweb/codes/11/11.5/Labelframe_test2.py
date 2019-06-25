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
        self.lf = ttk.Labelframe(self.master, padding=20)
        self.lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        # 创建一个显示图片的Label
        bm = PhotoImage(file='images/z.png')
        lb = Label(self.lf, image=bm)
        lb.bm = bm
        # 将Labelframe的标题设为显示图片的Label
        self.lf['labelwidget'] = lb
        # 定义代表Labelframe的标题位置的12个常量
        self.books = ['e', 's', 'w', 'n', 'es', 'ws', 'en', 'wn',
            'ne', 'nw', 'se', 'sw']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个Radiobutton，并放入Labelframe中
        for book in self.books:
            Radiobutton(self.lf, text= book,
            value=i,
            command=self.change,
            variable=self.intVar).pack(side=LEFT)
            i += 1
        self.intVar.set(9)
    def change(self):
        # 通过labelanchor选项改变Labelframe的标题的位置
        self.lf['labelanchor'] = self.books[self.intVar.get()]
root = Tk()
root.title("Labelframe测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
