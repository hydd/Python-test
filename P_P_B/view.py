# -*- coding: utf-8 -*-
'''
数据库查询。
'''
import mysql.connector
from modle import Cardid
from modle import create_session
from modle import getEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine(
#     'mysql+mysqlconnector://root:123456@127.0.0.1:3306/test?charset=utf8',
#     echo=True)

# def create_session():
#     # 创建session对象:
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session


def query_info(session):  # 全部查询，条件查询后续完成
    for instance in session.query(Cardid).order_by(Cardid.nid):
        print(instance.name, instance.info, instance.price)

    # for nid, name in session.query(Cardid.nid, Cardid.name):
    #     print(nid, name)


def query_info_by_name(session, name):
    for instance in session.query(Cardid).filter(
            Cardid.name.like('%' + name + '%')).all():
        print(instance.name, instance.info, instance.price)


def query_info_by_price(session, price):
    for instance in session.query(Cardid).filter(Cardid.price == price).all():
        print(instance.name, instance.info, instance.price)


if __name__ == '__main__':
    session = create_session(getEngine())
    query_info(session)
    query_info_by_name(session, '红米')
    query_info_by_price(session, '899')
