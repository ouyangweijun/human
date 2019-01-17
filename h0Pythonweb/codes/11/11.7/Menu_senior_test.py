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
from collections import OrderedDict

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 初始化菜单、工具条用到的图标
        self.init_icons()
        # 调用init_menu初始化菜单
        self.init_menu()
        # 调用init_toolbar初始化工具条
        self.init_toolbar()
        #---------------------------------
        # 创建、添加左边的Frame容器
        leftframe = ttk.Frame(self.master, width=40)
        leftframe.pack(side=LEFT, fill=Y)
        # 在左边窗口放一个Listbox
        lb = Listbox(leftframe, font=('Courier New', 20))
        lb.pack(fill=Y, expand=YES)
        for s in ('Python', 'Ruby', 'Swift', 'Kotlin', 'Java'):
            lb.insert(END, s)
        # 创建、添加右边的Frame容器
        mainframe = ttk.Frame(self.master)
        mainframe.pack(side=LEFT, fill=BOTH)
        text = Text(mainframe, width=40, font=('Courier New', 16))
        text.pack(side=LEFT, fill=BOTH)
        scroll = ttk.Scrollbar(mainframe)
        scroll.pack(side=LEFT,fill=Y)
        # 设置滚动条与text组件关联
        scroll['command'] = text.yview
        text.configure(yscrollcommand=scroll.set)
    # 创建菜单
    def init_menu(self):
        '初始化菜单的方法'
        # 定义菜单条所包含的3个菜单
        menus = ('文件', '编辑', '帮助')
        # 定义菜单数据
        items = (OrderedDict([
                # 每项对应一个菜单项，后面元组第一个元素是菜单图标，
                # 第二个元素是菜单对应的事件处理函数
                ('新建', (self.master.filenew_icon, None)),
                ('打开', (self.master.fileopen_icon, None)),
                ('保存', (self.master.save_icon, None)),
                ('另存为...', (self.master.saveas_icon, None)),
                ('-1', (None, None)),
                ('退出', (self.master.signout_icon, None)),
                ]),
            OrderedDict([('撤销',(None, None)),
                ('重做',(None, None)),
                ('-1',(None, None)),
                ('剪切',(None, None)),
                ('复制',(None, None)),
                ('粘贴',(None, None)),
                ('删除',(None, None)),
                ('选择',(None, None)),
                ('-2',(None, None)),
                # 二级菜单
                ('更多', OrderedDict([
                    ('显示数据',(None, None)),
                    ('显示统计',(None, None)),
                    ('显示图表',(None, None))
                    ]))
                ]),
            OrderedDict([('帮助主题',(None, None)),
                ('-1',(None, None)),
                ('关于', (None, None))]))
        # 使用Menu创建菜单条
        menubar = Menu(self.master)
        # 为窗口配置菜单条，也就是添加菜单条
        self.master['menu'] = menubar
        # 遍历menus元组
        for i, m_title in enumerate(menus):
            # 创建菜单
            m = Menu(menubar, tearoff=0)
            # 添加菜单
            menubar.add_cascade(label=m_title, menu=m)
            # 将当前正在处理的菜单数据赋值给tm
            tm = items[i]
            # 遍历OrderedDict,默认只遍历它的key
            for label in tm:
                print(label)
                # 如果value又是OrderedDict，说明是二级菜单
                if isinstance(tm[label], OrderedDict):
                    # 创建子菜单、并添加子菜单
                    sm = Menu(m, tearoff=0)
                    m.add_cascade(label=label, menu=sm)
                    sub_dict = tm[label]
                    # 再次遍历子菜单对应的OrderedDict，默认只遍历它的key
                    for sub_label in sub_dict:
                        if sub_label.startswith('-'):
                            # 添加分隔条
                            sm.add_separator()
                        else:
                            # 添加菜单项
                            sm.add_command(label=sub_label,image=sub_dict[sub_label][0],
                                command=sub_dict[sub_label][1], compound=LEFT)
                elif label.startswith('-'):
                    # 添加分隔条
                    m.add_separator()
                else:
                    # 添加菜单项
                    m.add_command(label=label,image=tm[label][0], 
                        command=tm[label][1], compound=LEFT)
    # 生成所有需要的图标
    def init_icons(self):
        self.master.filenew_icon = PhotoImage(file='images/filenew.png')
        self.master.fileopen_icon = PhotoImage(file='images/fileopen.png')
        self.master.save_icon = PhotoImage(file='images/save.png')
        self.master.saveas_icon = PhotoImage(file='images/saveas.png')
        self.master.signout_icon = PhotoImage(file='images/signout.png')
    # 生成工具条
    def init_toolbar(self):
        # 创建并添加一个Frame作为工具条的容器
        toolframe = Frame(self.master, height=20, bg='lightgray')
        toolframe.pack(fill=X) # 该Frame容器放在窗口顶部
        # 再次创建并添加一个Frame作为工具按钮的容器
        frame = ttk.Frame(toolframe)
        frame.pack(side=LEFT) # 该Frame容器放在容器左边
        # 遍历self.master的全部数据，根据系统图标来创建工具栏按钮
        for i, e in enumerate(dir(self.master)):
            # 只处理属性名以_icon结尾的属性（这些属性都是图标）
            if e.endswith('_icon'):
                ttk.Button(frame, width=20, image=getattr(self.master, e), 
                    command=None).grid(row=0, column=i, padx=1, pady=1, sticky=E)
root = Tk()
root.title("菜单测试")
# 禁止改变窗口大小
root.resizable(width=False, height=True)
App(root)
root.mainloop()
