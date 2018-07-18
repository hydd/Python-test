# -*- coding: utf-8 -*-
import csv
'''
将爬虫结果保存到 MySQL 关系型数据库中。
'''
import mysql.connector
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


def getEngine():
    engine = create_engine(
        'mysql+mysqlconnector://root:123456@127.0.0.1:3306/test?charset=utf8',
        echo=False)
    return engine


Base = declarative_base()


def read_file():
    # 先从文件中读取内容，储存在列表中
    code_list = []
    i = 1000
    with open('../test.csv', 'r', encoding='GB18030') as file:  # 问题同3.py
        context = csv.reader(file)  # 读取所有行
        for line in context:
            code_list.append([i + 1000, line[0], line[1], line[2]])
            i += 1
            # print(line)
    print(code_list)
    return code_list

    # with open("test.csv","r") as csvfile:
    # reader = csv.reader(csvfile)
    # #这里不需要readlines
    # for line in reader:
    #     print line


class Cardid(Base):  # 和表对应的类
    __tablename__ = 'MI_products'
    nid = Column(Integer, primary_key=True)
    name = Column(String(100))
    info = Column(String(100))
    price = Column(String(100))

    def __init__(self, nid, name, info, price):
        self.nid = nid
        self.name = name
        self.info = info
        self.price = price


def create_table():
    Base.metadata.create_all(getEngine())


def create_session(engine):
    # 创建session对象:
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def insert_info(session, code_list):  # 添加
    for each in code_list:
        nid, name, info, price = int(each[0]), each[1], each[2], each[3]
        print(nid, name, info, price)
        # 创建新User对象:
        new_code = Cardid(nid, name, info, price)
        # 添加到session:
        session.add(new_code)
        # 提交即保存到数据库:
        session.commit()
    # 关闭session:
    session.close()


# def query_info(session):  # 全部查询，条件查询后续完成
#     for instance in session.query(Cardid).order_by(Cardid.nid):
#         print(instance.name, instance.info, instance.price)

# for nid, name in session.query(Cardid.nid, Cardid.name):
#     print(nid, name)

if __name__ == '__main__':
    create_table()
    session = create_session(getEngine())
    code_list = read_file()
    insert_info(session, code_list)
    # query_info(session)
