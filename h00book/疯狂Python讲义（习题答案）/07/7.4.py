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
while True:
    st = input("请输入3个点的x、y值(空格隔开): ")
    if st == 'exit':
        import sys
        sys.exit(0)
    try:
        x1_st, y1_st, x2_st, y2_st, x3_st, y3_st = st.split()
        x1, y1, x2, y2, x3, y3 = float(x1_st), float(y1_st), float(x2_st), float(y2_st), float(x3_st), float(y3_st)
        if x1 == 0 and x2 == 0 and x3 == 0:
            print('处于同一条直线')
        elif 0 in (x1, x2, x3):
            print('不处于同一条直线')
        elif y1 / x1 == y2 / x2 and y1 / x1 == y3 / x3:
            print('处于同一条直线')
        else:
            print('不处于同一条直线')
    except:
        print('必须输入6个空格隔开的数')
    
