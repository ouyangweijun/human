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
        # 定义StringVar变量
        self.v = StringVar()
        # 创建Listbox组件，与v变量绑定
        self.lb = Listbox(topF, listvariable = self.v)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in range(20):  
            self.lb.insert(END, str(item))
        # 创建Scrollbar组件，设置该组件与self.lb的纵向滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        f = Frame(self.master)
        f.pack()
        Button(f, text="选中10项", command=self.select).pack(side=LEFT)
        Button(f, text="清除选中3项", command=self.clear_select).pack(side=LEFT)
        Button(f, text="删除3项", command=self.delete).pack(side=LEFT)
        Button(f, text="绑定变量", command=self.var_select).pack(side=LEFT)
    def select(self):
        # 选中指定项
        self.lb.selection_set(0, 9)  
    def clear_select(self):
        # 取消选中指定项
        self.lb.selection_clear(1,3)
    def delete(self):
        # 删除指定项
        self.lb.delete(5, 8)
    def var_select(self):
        # 修改与Listbox绑定的变量
        self.v.set(('12', '15'))      
root = Tk()
root.title("Listbox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
