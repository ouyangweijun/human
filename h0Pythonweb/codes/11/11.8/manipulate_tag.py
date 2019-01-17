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

# 创建窗口
root = Tk()
root.title('操作标签')
# 创建并添加Canvas
cv = Canvas(root, background='white', width=620, height=250)
cv.pack(fill=BOTH, expand=YES)
# 绘制一个矩形框
rt = cv.create_rectangle(40, 40, 300, 220,
    outline='blue', width=2,
    tag = ('t1', 't2', 't3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的id，也就是编号
print(rt) # 1
# 绘制一个椭圆
oval = cv.create_oval(350, 50, 580, 200,
    fill='yellow', width=0,
    tag = ('g1', 'g2', 'g3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的id，也就是编号
print(oval) # 2
# 根据指定tag该tag对应的所有图形项
print(cv.find_withtag('tag4')) # (1, 2)
# 获取指定图形项的所有tag
print(cv.gettags(rt))  # ('t1', 't2', 't3', 'tag4')
print(cv.gettags(2))  # ('g1', 'g2', 'g3', 'tag4')
cv.dtag(1, 't1') # 删除id为1的图形项上名为t1的tag
cv.dtag(oval, 'g1') # 删除id为oval的图形项上名为g1的tag
# 获取指定图形项的所有tag
print(cv.gettags(rt))  # ('tag4', 't2', 't3')
print(cv.gettags(2))  # ('tag4', 'g2', 'g3')
# 为所有图形项添加tag
cv.addtag_all('t5')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5')
# 为指定图形项添加tag
cv.addtag_withtag('t6', 'g2')
# 获取指定图形项的所有tag
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6')
# 为指定图形项上面的图形项添加tag, t2上面的就是oval图形项
cv.addtag_above('t7', 't2')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7')
# 为指定图形项下面的图形项添加tag, g2下面的就是rt图形项
cv.addtag_below('t8', 'g2')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7')
# 为最接近指定点的图形项添加tag，最接近360、90的图形项是oval
cv.addtag_closest('t9', 360, 90)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9')
# 为位于指定区域内（几乎覆盖整个图形区）的最上面的图形项添加tag
cv.addtag_closest('t10', 30, 30, 600, 240)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9', 't10')
# 为与指定区域内重合的最上面的图形项添加tag
cv.addtag_closest('t11', 250, 30, 400, 240)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9', 't10', 't11')
root.mainloop()
