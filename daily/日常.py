# -*- coding: utf-8 -*-
# __author__ = 'k.'
# 172.17.11.29
import pymysql

db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="root111",
    db="test",
    charset="utf8"
)

cursor = db.cursor()
sql = "INSERT INTO area (id, aname, lv, pid) VALUES ( %d, '%s', %d, %d )"
sql2 = "select *from area"
# data = (110105000001, '朝阳区', 3, 110100000001)
# cursor.execute(sql % data)
cursor.execute(sql2)
data = cursor.fetchone()
print(data)
# db.commit()
# print('成功插入', cursor.rowcount, '条数据')
db.close()

#https://github.com/jlhuang9/ChineseRegion/blob/master/ChineseRegion/spiders/MySql.py
#https://github.com/lawlite19/PythonCrawler-Scrapy-Mysql-File-Template/blob/master/webCrawler_scrapy/pipelines.py