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
        # 创建Style
        style = ttk.Style()
        style.configure("fkit.TPanedwindow", background='darkgray', relief=RAISED)
        # 创建Panedwindow组件，通过style属性配置分隔线
        pwindow = ttk.Panedwindow(self.master,
            orient=VERTICAL, style="fkit.TPanedwindow")  
        pwindow.pack(fill=BOTH, expand=1)
        first = ttk.Label(pwindow, text="第一个标签")
        # 调用add方法添加组件，每个组件一个区域
        pwindow.add(first)
        okBn = ttk.Button(pwindow, text="第二个按钮",
            # 调用remove()方法删除组件，该组件所在区域消失
            command=lambda : pwindow.remove(okBn))
        # 调用add方法添加组件，每个组件一个区域
        pwindow.add(okBn)
        entry = ttk.Entry(pwindow, width=30)
        # 调用add方法添加组件，每个组件一个区域
        pwindow.add(entry)
        # 调用insert方法插入组件
        pwindow.insert(1, Label(pwindow, text='插入的标签'))
root = Tk()
root.title("Panedwindow测试")
App(root)
root.mainloop()
