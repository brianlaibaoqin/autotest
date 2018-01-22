# -*- encoding:utf8 -*-
'''
@author: crazyant.net
@version: 2013-10-22

封装的mysql常用函数
'''

import pymysql


class DB():
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME

        self.conn = self.getConnection()

    def getConnection(self):
        return pymysql.Connect(
            host=self.DB_HOST,  # 设置MYSQL地址
            port=self.DB_PORT,  # 设置端口号
            user=self.DB_USER,  # 设置用户名
            passwd=self.DB_PWD,  # 设置密码
            db=self.DB_NAME,  # 数据库名
            charset='utf8'  # 设置编码
        )

    def query(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        returnData = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return returnData

    def update(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        self.conn.commit()
        cursor.close()
        self.conn.close()


if __name__ == "__main__":
    from data.datainfo import *
    db = DB('120.79.13.73',3306,'root', 'root', 'ymtest')
    #print(db.query("show tables;"))
    username = "autotest11"
    strSql = 'DELETE from`onethink_ucenter_member` WHERE `username` = %r ' % username
    db.update(strSql)
