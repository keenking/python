# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HomeScrapyItem(scrapy.Item):

    # provinceName = scrapy.Field()  # 省/直辖市/自治区名称
    #
    # cityName = scrapy.Field()      # 市/区级名称
    # cityNumber = scrapy.Field()
    #
    # countryName = scrapy.Field()   # 区/县级名称
    # countryNumber = scrapy.Field()
    #
    # townName = scrapy.Field()      # 乡/镇级名称
    # townNumber = scrapy.Field()
    #
    # villageName = scrapy.Field()   # 街道/镇/村级名称
    # villageNumber = scrapy.Field()
    # villageCode = scrapy.Field()
      id = scrapy.Field()     #行政区划代码
      aname = scrapy.Field()  #行政区划名称
      lv = scrapy.Field()     #行政区划等级
      pid = scrapy.Field()    #上级行政区划代码

