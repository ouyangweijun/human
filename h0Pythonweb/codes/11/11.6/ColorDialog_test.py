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
# 导入colorchooser
from tkinter import colorchooser
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建1个按钮，并为之绑定事件处理函数
        ttk.Button(self.master, text='选择颜色',
            command=self.choose_color # 绑定choose_color方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
    def choose_color(self):
        # 调用askcolor函数获取选中的颜色
        print(colorchooser.askcolor(parent=self.master, title='选择画笔颜色', 
            color = 'blue')) # 初始颜色
root = Tk()
root.title("颜色对话框测试")
App(root)
root.mainloop()
