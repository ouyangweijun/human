#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019-06-25 23:56
# @Author   : henry_oulen
# @Software : PyCharm
# @File     : hellp.py
# @Desc     :

import pymysql

import tornado.ioloop
import tornado.web
from tornado.options import define,options,parse_config_file,parse_command_line

define('port',default=80,type=int)


def main():
    pass


class DaysHandler(tornado.web.RequestHandler):
    # def get(self, year, month, day):
    def get(self, month, day, year):

        self.write('%s年%s月%s日' % (year, month, day))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name  = self.get_argument('name')
        print(name)
        self.write('hello world')

    def post(self):
        name  = self.get_argument('name')
        print(name)
        self.write('hello tornado')
class EntryHandler(tornado.web.RequestHandler):

    def initialize(self):
        # 实现功能是，访问flask9数据库，查询出学生的所有信息
        self.conn = pymysql.Connection(host='127.0.0.1', password='79892649',
                                  database='flask9', user='oulen',
                                  port=3306)
        self.cursor = self.conn.cursor()
        print('initialize')

    def prepare(self):
        print('prepare')

    def get(self):
        print('get')
        sql = 'select * from stu;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
        self.write('查询数据')

    def post(self):
        pass

    def on_finish(self):
        # 最后执行的方法
        print('on_finish')
        self.conn.close()

class IndexHandler(tornado.web.RequestHandler):

    def get(self):

        self.render('index.html')



def make_app():
    return tornado.web.Application(handlers=
                                   [
                                       (r'/', MainHandler),
                                       (r'/days/(\d{4})/(\d+)/(\d{2})/', DaysHandler),
                                       (r'/entry_point/', EntryHandler),
                                       (r'/index/', IndexHandler),

                                   ],
    template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

    )



if __name__ == '__main__':
    import os

    print(os.path.dirname(os.path.abspath(__file__)))
    a = os.path.dirname(os.path.abspath(__file__))


    # 解析启动命令 python xxx.py  --port=端口号
    parse_command_line()
    app = make_app()
    # 监听端口
    app.listen(options.port)
    # 监听启动的IO实例
    tornado.ioloop.IOLoop.current().start()
