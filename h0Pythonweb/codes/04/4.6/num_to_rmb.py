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
'''
  把一个浮点数分解成整数部分和小数部分字符串
  num 需要被分解的浮点数
  返回分解出来的整数部分和小数部分。
  第一个数组元素是整数部分，第二个数组元素是小数部分
'''
def divide(num):
    # 将一个浮点数强制类型转换为int型，即得到它的整数部分
    integer = int(num)
    # 浮点数减去整数部分，得到小数部分，小数部分乘以100后再取整得到2位小数
    fraction = round((num - integer) * 100)
    # 下面把整数转换为字符串
    return (str(integer), str(fraction))

han_list = ["零" , "壹" , "贰" , "叁" , "肆" ,\
    "伍" , "陆" , "柒" , "捌" , "玖"]
unit_list = ["十" , "百" , "千"]
'''
  把一个四位的数字字符串变成汉字字符串
  num_str 需要被转换的四位的数字字符串
  返回四位的数字字符串被转换成汉字字符串
'''
def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str)
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len) :
        # 把字符串转成数值
        num = int(num_str[i])
        # 如果不是最后一位数字，而且数字不是零，则需要添加单位（千、百、十）
        if i != num_len - 1 and num != 0 :
            result += han_list[num] + unit_list[num_len - 2 - i]
        # 否则不要添加单位
        else :
            result += han_list[num]
    return result
'''
  把数字字符串变成汉字字符串
  num_str 需要被转换的数字字符串
  返回数字字符串被转换成汉字字符串
'''
def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12 :
        print('数字太大，翻译不了')
        return
    # 如果大于8位，包含单位亿
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + "亿" + \
            four_to_hanstr(num_str[-8: -4]) + "万" + \
            four_to_hanstr(num_str[-4:])
    # 如果大于4位，包含单位万
    elif str_len > 4:
        return four_to_hanstr(num_str[:-4]) + "万" + \
            four_to_hanstr(num_str[-4:])
    else:
        return four_to_hanstr(num_str)
num = float(input("请输入一个浮点数: "))
# 测试把一个浮点数分解成整数部分和小数部分
integer, fraction = divide(num)
# 测试把一个四位的数字字符串变成汉字字符串
print(integer_to_str(integer))
print(fraction)