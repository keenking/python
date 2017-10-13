# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThetwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    provinceName = scrapy.Field()  # 省/直辖市/自治区名称

    cityName = scrapy.Field()      # 市/区级名称
    cityNumber = scrapy.Field()

    countryName = scrapy.Field()   # 区/县级名称
    countryNumber = scrapy.Field()

    townName = scrapy.Field()      # 乡/镇级名称
    townNumber = scrapy.Field()

    villageNumber = scrapy.Field()   # 街道/镇/村级名称
    villageCode = scrapy.Field()
    villageName = scrapy.Field()   # 最后村级名称





