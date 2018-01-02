# -*- coding: utf-8 -*-
# ORM框架 把关系型数据库的表结构映射到对象上
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类
Base = declarative_base()
# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    username = Column(String(21), primary_key=True)
    password = Column(String(21))

engine = create_engine('mysql+mysqlconnector://root:swj19961226@localhost:3306/test')
DBSession = sessionmaker(bind=engine)  # 可视为当前数据库连接
session = DBSession()
# session.add(User(username='寿爸爸', password='123'))
# session.commit()
user = session.query(User).filter(User.username=='xhy').one()
session.close()
print('Type:', type(user))
print('password:', user.password)
