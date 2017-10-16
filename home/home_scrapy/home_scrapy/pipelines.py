# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import threading
import pymysql
from DBUtils.PooledDB import PooledDB
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
        #  创建数据库连接池类方法
        dbpool = PooledDB(creator=pymysql,
                 mincached=settings['DB_MIN_CACHED'], maxcached=settings['DB_MAX_CACHED'],
                 maxshared=settings['DB_MAX_SHARED'], maxconnections=settings['DB_MAX_CONNECTIONS'],
                 blocking=settings['DB_BLOCKING'], maxusage=settings['DB_MAX_USAGE'], setsession=settings['DB_SET_SESSION'],
                 host=settings['DB_HOST'], port=settings['DB_PORT'],
                 user=settings['DB_USER'], passwd=settings['DB_PASSWD'],
                 db=settings['DB_NAME'], charset=settings['DB_CHARSET'], use_unicode=False
                 )
        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):
        lock.acquire()
        conn = self.dbpool.connection()
        cursor = conn.cursor()
        sql = "insert into area(id, aname, lv, pid) values(%s,%s,%s,%s)"
        params = (item["id"], item["aname"], item["lv"], item["pid"])
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()
        conn.close()
        lock.release()
        return item

