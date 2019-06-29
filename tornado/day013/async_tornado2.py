
import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.web.gen.coroutine()
    def get(self):
        q = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        respont = yield client.fetch('https://cn.bing.com/search?q=%s' % q)
        self.write('异步测试')

    # def on_response(self, response):
    #     # 回调，当页面响应，则调用回调函数on_response
    #     print(response)
    #     self.write('回调执行')
    #     self.finish()


def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', IndexHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
