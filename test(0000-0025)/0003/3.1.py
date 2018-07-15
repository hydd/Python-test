# -*- coding: utf-8 -*-
'''
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
import mysql.connector
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+mysqlconnector://root:123456@127.0.0.1:3306/test?charset=utf8',
    echo=True)
Base = declarative_base()


def read_file():
    # 先从文件中读取优惠码，储存在列表中
    code_list = []
    with open('../0001/code.txt',
              'r') as file:  # 问题同3.py
        context = file.readlines()  # 读取所有行
        for i in range(len(context)):
            code_list.append([i + 100, context[i]])  # 更新列表
    # print(code_list)
    return code_list


class Cardid(Base):  # 和表对应的类
    __tablename__ = 'Cardid_new'
    nid = Column(Integer, primary_key=True)
    val = Column(String(100))

    def __init__(self, nid, val):
        self.nid = nid
        self.val = val


def create_table():
    Base.metadata.create_all(engine)


def create_session():
    # 创建session对象:
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def insert_info(session, code_list):  # 添加
    for each in code_list:
        nid, val = int(each[0]), each[1]
        print(nid, val)
        # 创建新User对象:
        new_code = Cardid(nid, val)
        # 添加到session:
        session.add(new_code)
        # 提交即保存到数据库:
        session.commit()
    # 关闭session:
    session.close()


def query_info(session):  # 全部查询，条件查询后续
    for instance in session.query(Cardid).order_by(Cardid.nid):
        print(instance.val)

    for nid, val in session.query(Cardid.nid, Cardid.val):
        print(nid, val)


if __name__ == '__main__':
    create_table()
    session = create_session()
    code_list = read_file()
    insert_info(session, code_list)
    query_info(session)
