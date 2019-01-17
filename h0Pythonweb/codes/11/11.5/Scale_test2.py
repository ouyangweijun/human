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
        # 定义变量
        self.doubleVar = DoubleVar()
        self.scale = Scale(self.master,
            from_ = -100,  # 设置最大值
            to = 100,  # 设置最小值
            resolution = 5, # 设置步长
            label = '示范Sacle', # 设置标签内容
            length = 400, # 设置轨道的长度
            width = 30, # 设置轨道的宽度
            orient = HORIZONTAL,  #设置水平方向
            digits = 10, # 设置十位有效数字
            command = self.change, # 绑定事件处理函数
            variable = self.doubleVar # 绑定变量
        )
        self.scale.pack()
        # 设置Scale的当前值
        self.scale.set(20)
    # 这个事件处理函数比较奇葩，它可以接收到Scale的值
    def change(self, value):
        print(value, self.scale.get(), self.doubleVar.get())
root = Tk()
root.title("Scale测试")
App(root)
root.mainloop()
