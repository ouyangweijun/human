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
from selenium import webdriver
import time

# 通过executable_path指定浏览器驱动的路径
browser = webdriver.Firefox(executable_path="WeiboSpider/geckodriver.exe")
# 等待3秒，用于等待浏览器启动完成
time.sleep(3)
# 浏览指定网页
browser.get("http://www.crazyit.org/")
# 暂停5秒
time.sleep(5)
