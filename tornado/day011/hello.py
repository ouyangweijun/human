import os
from datetime import datetime, timedelta

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import pymysql

# 定义默认启动的端口port为80
define('port', default=8080, type=int)


class MainHandler(tornado.web.RequestHandler):
    # 必须继承RequestHandler
    def get(self):
        # 接收参数
        name = self.get_argument('name')
        name = self.get_query_argument('name')

        # 渲染响应给浏览器的数据
        self.write('hello tornado')

    def post(self):
        # 接收参数
        name = self.get_argument('name')
        name = self.get_body_argument('name')

        self.write('hello tornado post')


class ResHandler(tornado.web.RequestHandler):

    def get(self):
        # make_response('<H2>....', 404)
        self.write('<h2>今天天气真好</h2>')
        # 设置响应状态码
        self.set_status(200)
        # 设置cookie, 其中的expire参数表示过期时间，到了过期时间，自动删除
        # self.set_cookie('token', '123456', expires_days=1)
        # out_time = datetime.now() + timedelta(days=1)
        # self.set_cookie('token123', '123456', expires=out_time)

        # 删除cookie中的token值
        # self.clear_cookie('token')
        # self.clear_all_cookies()

        # 跳转
        self.redirect('/')


class DaysHandler(tornado.web.RequestHandler):
    # def get(self, year, month, day):
    def get(self, month, day, year):

        self.write('%s年%s月%s日' % (year, month, day))

class Days2Handler(tornado.web.RequestHandler):
    # def get(self, year, month, day):
    def get(self, month, year, day):
        self.write('%s年%s月%s日' % (year, month, day))

    def post(self, month, year, day):
        self.write('post:只负责新增数据')

    def delete(self, month, year, day):
        self.write('delete: 只负责删除')

    def patch(self, month, year, day):
        self.write('patch: 修改部分属性')

    def put(self, month, year, day):
        self.write('put: 修改全部数据')


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
    # handlers参数中定义路由匹配地址
    return tornado.web.Application(handlers=[
        (r'/', MainHandler),
        (r'/res/', ResHandler),
        (r'/days/(\d{4})/(\d+)/(\d{2})/', DaysHandler),
        (r'/days2/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/', Days2Handler),
        (r'/entry_point/', EntryHandler),
        (r'/index/', IndexHandler),
    ],
    template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    )


if __name__ == '__main__':
    # 解析启动命令, python xxx.py  --port=端口号
    parse_command_line()
    # 启动
    app = make_app()
    # 监听端口
    app.listen(options.port)
    # 监听启动的IO实例
    tornado.ioloop.IOLoop.current().start()



