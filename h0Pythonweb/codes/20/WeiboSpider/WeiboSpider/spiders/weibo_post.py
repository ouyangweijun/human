# -*- coding: utf-8 -*-
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
import scrapy
from selenium import webdriver
import time

class WeiboPostSpider(scrapy.Spider):
    name = 'weibo_post'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']
    def __init__(self):
        # 定义保存登录成功之后的cookie的变量
        self.login_cookies = []
    # 定义发送请求的请求头
    headers = {
        "Referer": "https://weibo.com/login/",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }
    def get_cookies(self):
        '''使用Selenium模拟浏览器登录并获取cookies'''
        cookies = []
        browser = webdriver.Firefox(executable_path="geckodriver.exe")
        # 等待3秒，用于等待浏览器启动完成，否则可能报错
        time.sleep(3) 
        browser.get("https://weibo.com/login/")  #①
        # 获取输入用户名的文本框
        elem_user = browser.find_element_by_xpath('//input[@id="loginname"]')
        # 模拟输入用户名
        elem_user.send_keys('xxxxxx@sina.com') #②
        # 获取输入密码的文本框
        elem_pwd = browser.find_element_by_xpath('//input[@type="password"]')
        # 模拟输入密码
        elem_pwd.send_keys('yyyyyy')  #③
        # 获取提交按钮
        commit = browser.find_element_by_xpath('//a[@node-type="submitBtn"]')
        # 模拟单击提交按钮
        commit.click()  #④
        # 暂停10秒，等待浏览器登录完成
        time.sleep(10)
        #登录成功后获取cookie
        if "微博-随时随地发现新鲜事" in browser.title:
            self.login_cookies = browser.get_cookies()
        else:
            print("登录失败！")
    # start_requests方法会在parse方法之前执行，该方法可用于处理登录逻辑。
    def start_requests(self):
        self.get_cookies()
        print('=====================', self.login_cookies)
        # 开始访问登录后的内容
        return [scrapy.Request('https://weibo.com/lgjava/home',
            headers=self.headers,
            cookies=self.login_cookies,
            callback=self.parse)]

    # 解析服务器相应的内容
    def parse(self, response):
        print('~~~~~~~parse~~~~~')
        print("是否解析成功:", '疯狂软件李刚' in response.text)
