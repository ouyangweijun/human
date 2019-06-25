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
        topF = Frame(self.master)
        topF.pack(fill=Y, expand=YES)
        # 创建Listbox组件
        self.lb = Listbox(topF)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in range(20):  
            self.lb.insert(END, str(item))
        # 创建Scrollbar组件，设置该组件与self.lb的纵向滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        # 为双击事件绑定事件处理方法
        self.lb.bind("<Double-1>", self.click)
    def click(self, event):
        from tkinter import messagebox
        # 获取Listbox当前选中项
        messagebox.showinfo(title=None, message=str(self.lb.curselection()))
root = Tk()
root.title("Listbox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
