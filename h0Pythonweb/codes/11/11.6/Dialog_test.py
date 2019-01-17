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
# 导入simpledialog
from tkinter import simpledialog
# 导入dialog
from tkinter import dialog

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.msg = '《疯狂Java讲义》历时十年沉淀，现已升级到第4版，'+\
            '经过无数Java学习者的反复验证，被包括北京大学在内的大量985、'+\
            '211高校的优秀教师引荐为参考资料、选作教材。'
        # 创建2个按钮，并为之绑定事件处理函数
        ttk.Button(self.master, text='打开SimpleDialog',
            command=self.open_simpledialog # 绑定open_simpledialog方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
        ttk.Button(self.master, text='打开Dialog',
            command=self.open_dialog # 绑定open_dialog方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
    def open_simpledialog(self):
        # 使用simpledialog.SimpleDialog创建对话框
        d = simpledialog.SimpleDialog(self.master, # 设置该对话框所属的窗口
            title='SimpleDialog测试', # 标题
            text=self.msg,  # 内容
            buttons=["是", "否", "取消"],
            cancel=3,
            default=0 # 设置默认是哪个按钮得到焦点
        )
        print(d.go())  #①
    def open_dialog(self):
        # 使用dialog.Dialog创建对话框
        d = dialog.Dialog(self.master # 设置该对话框所属的窗口
            , {'title': 'Dialog测试',  # 标题
            'text':self.msg, # 内容
            'bitmap': 'question', # 图标
            'default': 0,  # 设置默认选中项
            # strings选项用于设置按钮
            'strings': ('确定',
                '取消',
                '退出')})
        print(d.num)  #②

root = Tk()
root.title("对话框测试")
App(root)
root.mainloop()
