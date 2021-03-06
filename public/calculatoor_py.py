#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-02 01:42
# @Author  : henru_oulen
# @Software: PyCharm
# @File    : calcuatoor_py.py
# @Desc    : 统计指定路径项目代码

# coding=utf-8
import os
import time
basedir = '/Users/ouyangweijun/PycharmProjects/human'
basedir1 = '/Users/ouyangweijun/PycharmProjects/oulen'
basedir2 = '/Users/ouyangweijun/PycharmProjects/QA_Django'
filelists = []
# 指定想要统计的文件类型
whitelist = ['php', 'py']
#遍历文件, 递归遍历文件夹中的所有
def getFile(basedir):
    global filelists
    for parent,dirnames,filenames in os.walk(basedir):
        #for dirname in dirnames:
        #    getFile(os.path.join(parent,dirname)) #递归
        for filename in filenames:
            ext = filename.split('.')[-1]
            #只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent,filename))
#统计一个文件的行数
def countLine(fname):
    count = 0
    for file_line in open(fname).readlines():
        if file_line != '' and file_line != '\n': #过滤掉空行
            count += 1
    print (fname + '----' , count)
    return count

def main(base):
    startTime = time.time()
    getFile(base)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print ('total lines:',totalline)
    print ('Done! Cost Time: %0.2f second' % (time.time() - startTime))

if __name__ == '__main__' :
    #human = main(basedir)
    oulen = main(basedir1)
    #Qa_django = main(basedir2)
