# -*- coding: utf-8 -*-
# __author__ = 'k.'
import pymysql
from DBUtils.PooledDB import PooledDB
from scrapy.utils.project import get_project_settings


# 创建数据库连接池类
class dbconnectPool(object):
    __pool = None

    def __enter__(self):
        self.conn = self.getConn()
        self.cursor = self.conn.cursor
        return self

    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置，设置需要的信息
        self.host = self.settings['DB_HOST']
        self.port = self.settings['DB_PORT']
        self.user = self.settings['DB_USER']
        self.passwd = self.settings['DB_PASSWD']
        self.db = self.settings['DB_NAME']
        self.charset = self.settings['DB_CHARSET']
        self.mincached = self.settings['DB_MIN_CACHED']
        self.maxcached = self.settings['DB_MAX_CACHED']
        self.maxconnections = self.settings['DB_MAX_CONNECTIONS']
        self.blocking = self.settings['DB_BLOCKING']
        self.maxusage = self.settings['DB_MAX_USAGE']
        self.setsession = self.settings['DB_SET_SESSION']
        self.maxshared = self.settings['DB_MAX_SHARED']

    def getConn(self):
        if self.__pool is None:
            self.__pool = PooledDB(creator=pymysql,
                                   mincached=self.mincached, maxcached=self.maxcached,
                                   maxshared=self.maxshared, maxconnections=self.maxconnections,
                                   blocking=self.blocking, maxusage=self.maxusage, setsession=self.setsession,
                                   host=self.host, port=self.port,
                                   user=self.user, passwd=self.passwd,
                                   db=self.db, charset=self.charset, use_unicode=False
                                   )
            return self.__pool.connection()

#释放数据库连接池
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.cursor.close()
    #     self.conn.close()

#获取数据库连接池连接
def getdbconnectPool():
    return dbconnectPool()
