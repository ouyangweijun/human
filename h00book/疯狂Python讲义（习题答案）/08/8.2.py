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
start = 100
end = 999
nums = end - start + 1
def check_key (key):
    if not isinstance(key, int): raise TypeError('索引值必须是整数')
    if key < 0: raise IndexError('索引值必须是非负整数')
    if key >= nums: raise IndexError('索引值不能超过%d' % nums) 
def check_value (value):
    if not isinstance(value, int): raise TypeError('序列值必须是整数')
    if not (end >= value >= start): raise IndexError('序列值必须在%d和%d之间' % (start, end)) 

class NumSeq:
    def __init__(self):
        self.__changed = {}
        self.__deleted = []
    def __len__(self):
        return nums
    def __getitem__(self, key):
        check_key(key)
        # 如果在self.__changed中找到已经修改后的数据
        if key in self.__changed :
            return self.__changed[key]
        # 如果key在self.__deleted中，说明该元素已被删除
        if key in self.__deleted :
            return None
        return start + key
    def __setitem__(self, key, value):
        check_key(key)
        check_value(value)
        self.__changed[key] = value
    def __delitem__(self, key):
        check_key(key)
        # 如果__deleted列表中没有包含被删除key，添加被删除的key
        if key not in self.__deleted : self.__deleted.append(key)
        # 如果__changed中包含被删除key，删除它
        if key in self.__changed : del self.__changed[key]

if __name__ == '__main__':
    nq = NumSeq()
    print(len(nq))
    print(nq[2]) # 101
    print(nq[1]) # 100
    # 修改nq[1]元素
    nq[1] = 123
    # 打印修改之后的nq[1]
    print(nq[1]) # 123
    # 删除nq[1]
    del nq[1]
    print(nq[1]) # None
    # 再次对nq[1]赋值
    nq[1] = 987
    print(nq[1]) # 987
