# -*- coding: utf-8 -*-
'''
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
import mysql.connector


def read_file():
    # 先从文件中读取优惠码，储存在列表中
    code_list = []
    # with open(r'./test(0000-0025)/0001/code.txt',
    with open(
            r'../0001/code.txt',
            'r') as file:  # 经过测试发现coderunner运行.py时当前目录为coderunner调用python时的路径，
        # 和.py所在位置无关。因此只要.py不在coderunner调用python所在路径下，jitest文件夹直接子文件，
        # 二十子文件夹文件，那么正确写法相对路径时无法识别的，需要改为以上注释方可以。
        # 但是这样，.py将只能通过coderunner运行。因此，决定使用正确相对路径写法，通过cmd窗口进行运行。

        # python终端似乎具有同样问题，因此涉及到相对路径还是使用cmd进行运行
        context = file.readlines()  # 读取所有行
        for i in range(len(context)):
            code_list.append([i, context[i]])  # 更新列表
    # print(code_list)
    return code_list


def insert_db(code_list):  # 通过sql语句进行数据库操作略显复杂，后续尝试通过ORM框架来进行相关操作
    # 连接数据库
    connect = mysql.connector.connect(
        user='root', password='123456', host='127.0.0.1', database='test')

    # 获取游标
    cursor = connect.cursor()

    # 查询数据
    # sql = "SELECT * FROM code_id"
    sql = 'insert into code_id(id,val) values(%s,%s)'  # 使用通配符写sql语句，之后可以进行替换
    for each in code_list:
        cursor.execute(sql, each)  # 通过迭代将整个列表insert到表中
    connect.commit()  # 数据增加之后要提交一下才能insert到库中，第一次忘记提交导致之后的select可以
    # 查询到增加信息，但并没有真正insert成功，数据库表中无法查到

    sql = "SELECT * FROM code_id"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print("id:%s\nname:%s" % row)
    print('共查找出', cursor.rowcount, '条数据')

    # 关闭连接
    cursor.close()
    connect.close()


def read_insert():
    code = read_file()
    insert_db(code)


if __name__ == '__main__':
    # read_insert()
    read_file()
