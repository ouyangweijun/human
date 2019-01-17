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
        # ttk使用Combobox取代了Listbox
        cb = ttk.Combobox(self.master, font=24)
        # 为Combobox设置列表项
        cb['values'] = ('Python', 'Swift', 'Kotlin')
#        cb = Listbox(self.master, font=24)
        # 为Listbox设置列表项
#        for s in ('Python', 'Swift', 'Kotlin'):
#            cb.insert(END, s)
        cb.pack(side=LEFT, fill=X, expand=YES)
        f = ttk.Frame(self.master)
#        f = Frame(self.master)
        f.pack(side=RIGHT, fill=BOTH, expand=YES)
        lab = ttk.Label(self.master, text='我的标签', font=24)
#        lab = Label(self.master, text='我的标签', font=24)
        lab.pack(side=TOP, fill=BOTH, expand=YES)
        bn = ttk.Button(self.master, text='我的按钮')
#        bn = Button(self.master, text='我的按钮')
        bn.pack()
root = Tk()
root.title("简单事件处理")
App(root)
root.mainloop()