# -*- coding: utf-8 -*-
# __author__ = 'k.'
import pymysql
from scrapy.utils.project import get_project_settings


class DBHelper():
    #读取settings配置
    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置，设置需要的信息
        self.host = self.settings['DB_HOST']
        self.port = self.settings['DB_PORT']
        self.user = self.settings['DB_USER']
        self.passwd = self.settings['DB_PASSWD']
        self.db = self.settings['DB_DBNAME']
        self.charset = self.settings['DB_CHARSET']

    # 连接数据库
    def dbconnect(self):
        dbconn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            charset=self.charset
        )
        return dbconn
    #连接配置中的DB_DBNAME数据库
    def dbnameconnet(self):
        dbconn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset=self.charset
        )
        return dbconn
    #创建数据库
    def dbcreate(self):
        dbconn= self.dbconnect()
        cur = dbconn.cursor()
        sql = "create database if not exists "+self.db
        cur.execute(sql)
        cur.close()
        dbconn.close()
        return self
    #创建表
    def tbcreate(self, sql):
        dbconn = self.dbnameconnet()
        cur = dbconn.cursor()
        cur.execute(sql)
        cur.close()
        dbconn.close()
        return self
    #插入数据
    def insert_data(self,sql,*params):
        dbconn = self.dbnameconnet()
        cur = dbconn.cursor()
        cur.execute(sql, params)
        dbconn.commit()
        cur.close()
        dbconn.close()
if __name__ == '__main__':
    a = DBHelper()
    sql = "DROP TABLE IF EXISTS area;" \
          "CREATE TABLE area(id INT (20) primary key auto_increment, " \
          "aname VARCHAR (128)," \
          "lv INT (4)," \
          "pid INT (20))"
    sql2 = "insert into area(id, aname, lv, pid) VALUES (%s, %s, %s, %s)"
    params = (110107000001, '石景山区', 3, 110100000000)
    # a.tbcreate(sql)
    a.insert_data(sql2, *params)







