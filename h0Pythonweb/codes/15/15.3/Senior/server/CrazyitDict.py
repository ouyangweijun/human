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
class CrazyitDict(dict):
    # 根据value查找key
    def key_from_value(self, val):
        # 遍历所有key组成的集合
        for key in self.keys():
            # 如果指定key对应的value与被搜索的value相同，则返回对应的key
            if self[key] == val:
                return key
        return None
    # 根据value删除key
    def remove_by_value(self, val):
        # 遍历所有key组成的集合
        for key in self.keys():
            # 如果指定key对应的value与被搜索的value相同，则返回对应的key
            if self[key] == val:
                self.pop(key)
                return
