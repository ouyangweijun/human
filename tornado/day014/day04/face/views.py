
import tornado.web

from face.models import init_db, User
from utils.conn import Base, session
from utils.faceId import face_register, face_login


class RegisterHandler(tornado.web.RequestHandler):

    def get(self):
        error = ''
        self.render('register.html', error=error)

    def post(self):
        # 注册功能
        # 获取数据
        face = self.get_argument('face_img')
        img = face.split(',')[-1]
        username = self.get_argument('username')
        realname = self.get_argument('realname')
        if face and username and realname:
            # 注册（用户模型）
            user = User()
            user.username = username
            user.realname = realname
            session.add(user)
            session.commit()
            # 调用百度人脸注册接口
            res = face_register(img, user.id)
            if res:
                # 注册成功，跳转到登录
                self.redirect('/login/')
            else:
                # 注册失败，则跳转到注册
                session.delete(user)
                session.commit()
                self.redirect('/register/')
        else:
            error = '请填写完整的参数'
            self.render('register.html', error=error)


class InitDbHandler(tornado.web.RequestHandler):

    def get(self):
        # 将模型映射到数据库中
        # Base.metadata.create_all()
        init_db()

        self.write('创建表成功')


class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        face = self.get_argument('face_img')
        img = face.split(',')[-1]
        res = face_login(img)
        if res:
            self.write('登录成功')
        else:
            self.write('登录失败')

