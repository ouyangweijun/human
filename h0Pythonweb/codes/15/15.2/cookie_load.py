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
from urllib.request import *
import http.cookiejar, urllib.parse

# 以指定文件创建CookieJar对象，对象将可以把cookie保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 直接加载a.txt中的Cookie信息
cookie_jar.load('a.txt',ignore_discard=True,ignore_expires=True)
# 遍历a.txt中保存的cookie信息
for item in cookie_jar:
    print('Name ='+ item.name)
    print('Value ='+ item.value)
# 创建HTTPCookieProcessor对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建OpenerDirector对象
opener = build_opener(cookie_processor)

# 定义模拟Chrome浏览器的user_agent
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' \
    r' (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# 定义请求头
headers = {'User-Agent':user_agent, 'Connection':'keep-alive'}

#-------------下面代码发送访问被保护资源的GET请求----------------
# 创建向"受保护页面"发送GET请求的Request
request = Request('http://localhost:8888/test/secret.jsp',
    headers=headers)
response = opener.open(request)
print(response.read().decode())
