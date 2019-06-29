import os

import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

from app.views import LoginHandler, ChatHandler

define('port', default=80, type=int)


def make_app():
    return tornado.web.Application(handlers=[
        (r'/login/', LoginHandler),
        (r'/chat/', ChatHandler),
    ],
    template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
    static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
    cookie_secret='agdfiuwetr9w4689rfhjdc'
    )

if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


