
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from utils.conn import Base


def init_db():
    # 模型映射成表，定义的位置必须和模型定义在一个文件
    Base.metadata.create_all()

class User(Base):

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10), unique=True, nullable=False)
    realname = Column(String(10), unique=True, nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    __tablename__ = 'user'
