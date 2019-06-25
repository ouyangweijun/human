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
import json
# 定义JSONEncoder的子类
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        # 如果要转换的对象是复数类型，程序负责处理
        if isinstance(obj, complex):
            return {"__complex__": 'true', 'real': obj.real, 'imag': obj.imag}
        # 对于其他类型，还使用JSONEncoder的默认处理
        return json.JSONEncoder.default(self, obj)
s1 = json.dumps(2 + 1j, cls=ComplexEncoder)
print(s1) # '{"__complex__": "true", "real": 2.0, "imag": 1.0}'
s2 = ComplexEncoder().encode(2 + 1j)
print(s2) # '{"__complex__": "true", "real": 2.0, "imag": 1.0}'
