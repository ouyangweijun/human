from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado9'

engine = create_engine(db_url)

Base = declarative_base(bind=engine)

DbSession = sessionmaker(bind=engine)
session = DbSession()

