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
        self.sv = StringVar()
        # 创建一个OptionMenu控件
        self.om = ttk.OptionMenu(root,
            self.sv, # 绑定变量 
            'Python', # 设置初始选中值
            'Kotlin', # 以下多个值用于设置菜单项
            'Ruby',
            'Swift',
            'Java',
            'Python',
            'JavaScript',
            'Erlang',
            command = self.print_option) # 绑定事件处理方法
        self.om.pack()
        # 创建Labelframe容器
        lf = ttk.Labelframe(self.master, padding=20, text='请选择菜单方向')
        lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        # 定义代表Labelframe的标题位置的12个常量
        self.directions = ['below', 'above', 'left', 'right', 'flush']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个Radiobutton，并放入Labelframe中
        for direct in self.directions:
            Radiobutton(lf, text= direct,
            value=i,
            command=self.change,
            variable=self.intVar).pack(side=LEFT)
            i += 1
        self.intVar.set(9)
    def print_option(self, val):
        # 通过两种方式来获取OptionMenu选中的菜单项的值
        print(self.sv.get(), val)
    def change(self):
        # 通过direction选项改变OptionMenu上菜单的展开方向
        self.om['direction'] = self.directions[self.intVar.get()]
root = Tk()
root.title("OptionMenu测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
