# -*- coding:utf-8 -*-
# Author:oulen

"""
全局变量是否需需要global
"""


import time
import threading

num=100
nums=[11,22]
def test():
    global num
    num +=100

def test2():
    nums.append(12)
    print(nums)
print(nums)
print(num)

test()
test2()



# 1.在一个函数中，对全局变量进行修改时，是否需要使用global进行说明，要看是否对全局变量的执行指向进行修改
# 2.如是修改啦执行，即让全局变量执行一个新的地方，那么必须使用global  例如a+=100
# 3.如果是，仅仅是修改啦指向的空间中的数据，此时不用必须使用global 例如append
