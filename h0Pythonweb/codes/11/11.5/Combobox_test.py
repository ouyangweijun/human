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
        self.strVar = StringVar()
        # 创建Combobox组件
        self.cb = ttk.Combobox(self.master,
            textvariable=self.strVar, # 绑定到self.strVar变量
            postcommand=self.choose) # 当用户单击下拉箭头时触发self.choose方法
        self.cb.pack(side=TOP)
        # 为Combobox配置多个选项
        self.cb['values'] = ['Python', 'Ruby', 'Kotlin', 'Swift']
        f = Frame(self.master)
        f.pack()
        self.isreadonly = IntVar()
        # 创建Checkbutton，绑定到self.isreadonly变量
        Checkbutton(f, text = '是否只读:',
            variable=self.isreadonly,
            command=self.change).pack(side=LEFT)
        # 创建Button，单击该按钮激发setvalue方法
        Button(f, text = '绑定变量设置',
            command=self.setvalue).pack(side=LEFT)
    def choose(self):
        from tkinter import messagebox
        # 获取Combbox的当前值
        messagebox.showinfo(title=None, message=str(self.cb.get()))
    def change(self):
        self.cb['state'] = 'readonly' if self.isreadonly.get() else 'enable'
    def setvalue(self):
        self.strVar.set('我爱Python')
root = Tk()
root.title("Combobox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
