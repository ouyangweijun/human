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
from tkinter import colorchooser
import threading

# 创建窗口
root = Tk()
root.title('操作图形项')
# 创建并添加Canvas
cv = Canvas(root, background='white', width=400, height=350)
cv.pack(fill=BOTH, expand=YES)
# 该变量用于保存当前选中的图形项
current = None
# 该变量用于保存当前选中的图形项的边框颜色
current_outline = None
# 该变量用于保存当前选中的图形项的边框宽度
current_width = None
# 该函数用于高亮显示选中图形项（边框颜色会red、yellow之间切换）
def show_current():
    # 如果当前选中项不为None
    if current is not None:
        # 如果当前选中图形项的边框色为red，将它改为yellow
        if cv.itemcget(current, 'outline') == 'red':
            cv.itemconfig(current, width=2,
                outline='yellow')
        # 否则，将颜色改为red
        else:
             cv.itemconfig(current, width=2,
                outline='red')
    global t
    # 通过定时器指定0.2秒之后执行show_current函数
    t = threading.Timer(0.2, show_current)
    t.start()
# 通过定时器指定0.2秒之后执行show_current函数
t = threading.Timer(0.2, show_current)
t.start()
# 分别创建矩形、椭圆、和圆
rect = cv.create_rectangle(30, 30, 250, 200,
    fill='magenta', width='0')
oval = cv.create_oval(180, 50, 380, 180,
    fill='yellow', width='0')
circle = cv.create_oval(120, 150, 300, 330,
    fill='pink', width='0')
bottomF = Frame(root)
bottomF.pack(fill=X,expand=True)
liftbn = Button(bottomF, text='向上',
    # 将椭圆移动到它上面的item之上
    command=lambda : cv.tag_raise(oval, cv.find_above(oval)))
liftbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
lowerbn = Button(bottomF, text='向下',
    # 将椭圆移动到它下面的item之下
    command=lambda : cv.tag_lower(oval, cv.find_below(oval)))
lowerbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
def change_fill():
    # 弹出颜色选择框,让用户选择颜色
    fill_color = colorchooser.askcolor(parent=root, 
        title='选择填充颜色', 
        # 初始颜色设置为椭圆当前的填充色（fill选项值）
        color =  cv.itemcget(oval, 'fill'))
    if fill_color is not None:
        cv.itemconfig(oval, fill=fill_color[1])
fillbn = Button(bottomF, text='改变填充色',
    # 该按钮触发change_fill函数
    command=change_fill)
fillbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
def change_outline():
    # 弹出颜色选择框,让用户选择颜色
    outline_color = colorchooser.askcolor(parent=root, 
        title='选择边框颜色',
        # 初始颜色设置为椭圆当前的边框色（outline选项值）
        color = cv.itemcget(oval, 'outline'))
    if outline_color is not None:
        cv.itemconfig(oval, outline=outline_color[1],
            width=4)
outlinebn = Button(bottomF, text='改变边框色',
    # 该按钮触发change_outline函数
    command=change_outline)
outlinebn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
movebn = Button(bottomF, text='右下移动',
    # 调用move方法移动图形项
    command=lambda : cv.move(oval, 15, 10))
movebn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
coordsbn = Button(bottomF, text='位置复位',
    # 调用coords方法重设图形项的大小和位置
    command=lambda : cv.coords(oval, 180, 50, 380, 180))
coordsbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
# 再次添加Frame容器
bottomF = Frame(root)
bottomF.pack(fill=X,expand=True)
zoomoutbn = Button(bottomF, text='缩小',
    # 调用scale方法对图形项进行缩放
    # 前面两个坐标指定缩放中心，后面两个参数指定横向、纵向的缩放比
    command=lambda : cv.scale(oval, 180, 50, 0.8, 0.8))
zoomoutbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
zoominbn = Button(bottomF, text='放大',
    # 调用scale方法对图形项进行缩放
    # 前面两个坐标指定缩放中心，后面两个参数指定横向、纵向的缩放比
    command=lambda : cv.scale(oval, 180, 50, 1.2, 1.2))
zoominbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
def select_handler(ct):
    global current, current_outline, current_width
    # 如果ct元组包含了选中项
    if ct is not None and len(ct) > 0:
        ct = ct[0]
        # 如果current对应的图形项不为空
        if current is not None:
            # 恢复current对应的图形项的边框
            cv.itemconfig(current, outline=current_outline,
                width = current_width)
        # 获取当前选中图形项的边框信息
        current_outline = cv.itemcget(ct, 'outline')
        current_width = cv.itemcget(ct, 'width')
        # 使用current保存当前选中项
        current = ct    
def click_handler(event):
    # 获取当前选中的图形项
    ct = cv.find_closest(event.x, event.y)
    # 调用select _handler处理选中图形项
    select_handler(ct)
def click_select():
    # 取消为“框选”绑定的两个事件处理函数
    cv.unbind('<B1-Motion>')
    cv.unbind('<ButtonRelease-1>')
    # 为“点选”绑定鼠标点击的事件处理函数
    cv.bind('<Button-1>', click_handler)
clickbn = Button(bottomF, text='点选图形项',
    # 该按钮触发click_select函数
    command=click_select)
clickbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
# 记录鼠标拖动的第一个点的x、y坐标 
firstx = firsty = None
# 记录前一次绘制的、代表选择区的虚线框
prev_select = None
def drag_handler(event):
    global firstx, firsty, prev_select
    # 刚开始拖动时，用鼠标位置为firstx、firsty赋值
    if firstx is None and firsty is None:
        firstx, firsty = event.x, event.y
    leftx, lefty = min(firstx, event.x), min(firsty, event.y)
    rightx, righty = max(firstx, event.x), max(firsty, event.y)
    # 删除上一次绘制的虚线选择框
    if prev_select is not None:
        cv.delete(prev_select)
    # 重新绘制虚线选择框
    prev_select = cv.create_rectangle(leftx, lefty, rightx, righty, 
        dash=2)
def release_handler(event):
    global firstx, firsty
    if prev_select is not None:
        cv.delete(prev_select)
    if firstx is not None and firsty is not None:
        leftx, lefty = min(firstx, event.x), min(firsty, event.y)
        rightx, righty = max(firstx, event.x), max(firsty, event.y)
        firstx = firsty = None
        # 获取当前选中的图形项
        ct = cv.find_enclosed(leftx, lefty, rightx, righty)
        # 调用select _handler处理选中图形项
        select_handler(ct)
def rect_select():
    # 取消为“点选”绑定的事件处理函数
    cv.unbind('<Button-1>')
    # 为“框选”绑定鼠标拖动、鼠标释放的事件处理函数
    cv.bind('<B1-Motion>', drag_handler)
    cv.bind('<ButtonRelease-1>', release_handler)
rectbn = Button(bottomF, text='框选图形项',
    # 该按钮触发rect_select函数
    command=rect_select)
rectbn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
deletebn = Button(bottomF, text='删除',
    # 删除图形项
    command=lambda : cv.delete(oval))
deletebn.pack(side=LEFT, ipadx=10, ipady=5, padx=3)
root.mainloop()
