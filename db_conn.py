# pip install mysql-connector-python
# coding=utf-8
# !/usr/bin/python
import mysql.connector
# 连接数据库
connect = mysql.connector.connect(
    user='root', password='123456', host='127.0.0.1', database='test')

# 获取游标
cursor = connect.cursor()

# 查询数据
sql = "SELECT * FROM tt"
cursor.execute(sql)
for row in cursor.fetchall():
    print("id:%s\name:%s" % row)
print('共查找出', cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
connect.close()