# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import threading
# from home_scrapy.DB_connection_pool import getdbconnectPool
import pymysql
from DBUtils.PooledDB import PooledDB
from scrapy.utils.project import get_project_settings
class HomeScrapyPipeline(object):
    def __init__(self):
        self.f = open("data.json", 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ", \n"
        self.f.write(content.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.f.close()


lock = threading.RLock()
class HomeScrapyMySQLPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool


    @classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法。
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        dbpool = PooledDB(creator=pymysql,
                 mincached=settings['DB_MIN_CACHED'], maxcached=settings['DB_MAX_CACHED'],
                 maxshared=settings['DB_MAX_SHARED'], maxconnections=settings['DB_MAX_CONNECTIONS'],
                 blocking=settings['DB_BLOCKING'], maxusage=settings['DB_MAX_USAGE'], setsession=settings['DB_SET_SESSION'],
                 host=settings['DB_HOST'], port=settings['DB_PORT'],
                 user=settings['DB_USER'], passwd=settings['DB_PASSWD'],
                 db=settings['DB_NAME'], charset=settings['DB_CHARSET'], use_unicode=False
                 )
        dbpool = dbpool.connection()
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    # pipeline默认调用
    def process_item(self, item, spider):
            db = self.dbpool
            cursor = db.cursor()
            sql = "insert into area(id, aname, lv, pid) values(%s,%s,%s,%s)"
            params = (item["id"], item["aname"], item["lv"], item["pid"])
            cursor.execute(sql, params)
            db.commit()
            cursor.close()
            db.close()
            return item

