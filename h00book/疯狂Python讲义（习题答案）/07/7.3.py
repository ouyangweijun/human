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
def fn(tp):
    for e in tp:
        if not isinstance(e, str):
            raise ValueError('所有元素必须是字符串')
        if not (20 >= len(e) >= 6):
            raise ValueError('字符串的长度必须在6～20之间')
    print(tp)
    
if __name__ == '__main__':
    fn(('fkjava', 'crazyit'))
#    fn((20,))
    fn(('fkjavafkjavafkjavafkjava'))

        
        
    
