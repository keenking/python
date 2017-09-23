# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HomeScrapyItem(scrapy.Item):

    provinceName = scrapy.Field()  # 省/直辖市/自治区名称

    cityName = scrapy.Field()      # 市/区级名称

    countryName = scrapy.Field()   # 区/县级名称

    villageName = scrapy.Field()   # 街道/镇/村级名称

    streetName = scrapy.Field()   # 最后村级名称

    cityNumber = scrapy.Field()   # 城乡分类代码

    planNumber = scrapy.Field()   # 统计用区划代码
