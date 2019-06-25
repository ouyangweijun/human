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
import enum
class Orientation(enum.Enum):
    # 为序列值指定value值
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'
    def info(self):
        print('这是一个代表方向【%s】的枚举' % self.value)
print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
# 通过枚举变量名访问枚举
print(Orientation['WEST'])
# 通过枚举值来访问枚举
print(Orientation('南'))
# 调用枚举的info()方法
Orientation.EAST.info()
# 遍历Orientation枚举的所有成员
for name, member in Orientation.__members__.items():
    print(name, '=>', member, ',', member.value)