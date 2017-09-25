# -*- coding: utf-8 -*-
import scrapy
from home_scrapy.items import HomeScrapyItem
import os


class SpideroneSpider(scrapy.Spider):
    name = 'spiderone'
    allowed_domains = ['http://www.stats.gov.cn']
    baseUrl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html']

    # 省
    def parse(self, response):
        node_list = response.xpath('//tr[@class="provincetr"]/td/a')
        for province_node in node_list:
            province_data = HomeScrapyItem()
            name = province_node.xpath('text()').extract()
            url = province_node.xpath('@href').extract()
            province_data['provinceName'] = name[0]
            city_url = self.baseUrl + str(url[0])
            print(city_url)
            yield scrapy.Request(city_url, meta={'province_data': province_data}, callback=self.city_parse,
                                 encoding='utf-8', dont_filter=True)

    # 市

    def city_parse(self, response):
        city_list = response.xpath('//tr[@class="citytr"]')
        meta = response.meta['province_data']
        for city_node in city_list:
            city_data = dict(meta)
            number = city_node.xpath('td[1]/a/text()').extract()
            name = city_node.xpath('td[2]/a/text()').extract()
            city_url = city_node.xpath('td[1]/a/@href').extract()
            city_data['cityNumber'] = number[0]
            city_data['cityName'] = name[0]
            country_url = self.baseUrl + str(city_url[0])
            yield scrapy.Request(country_url, meta={'city_data': city_data}, callback=self.country_parse,
                                 encoding='utf-8', dont_filter=True)
            # 县

    def country_parse(self, response):
        meta = response.meta['city_data']
        country_list = response.xpath('//tr[@class="countytr"]')
        for country_node in country_list:

            if country_node.xpath('td/a/text()'):  # 此处if语句的判断耗时2小时，铭记。。
                country_data = dict(meta)
                number = country_node.xpath('td[1]/a/text()').extract()
                name = country_node.xpath('td[2]/a/text()').extract()
                country_data['countryNumber'] = number[0]
                country_data['countryName'] = name[0]
                country_url = country_node.xpath('td[1]/a/@href').extract()[0]
                base_link = os.path.dirname(response.url)
                next_link = '/'.join([base_link, country_url])
                yield scrapy.Request(next_link, meta={'country_data': country_data}, callback=self.town_parse,
                                     encoding='utf-8', dont_filter=True)
            else:
                country_data = dict(meta)
                number = country_node.xpath('td[1]/text()').extract()
                name = country_node.xpath('td[2]/text()').extract()
                country_data['countryNumber'] = number[0]
                country_data['countryName'] = name[0]
                yield country_data

    def town_parse(self, response):
        meta = response.meta['country_data']
        town_list = response.xpath('//tr[@class="towntr"]')
        for town_node in town_list:
            town_data = dict(meta)
            number = town_node.xpath('td[1]/a/text()').extract()
            name = town_node.xpath('td[2]/a/text()').extract()
            town_data['townNumber'] = number[0]
            town_data['townName'] = name[0]
            town_url = town_node.xpath('td[1]/a/@href').extract()[0]
            base_link = os.path.dirname(response.url)
            next_link = '/'.join(([base_link, town_url]))
            yield scrapy.Request(next_link, meta={'town_data': town_data}, callback=self.village_parse,
                                 encoding='utf-8', dont_filter=True)

    def village_parse(self, response):
        meta = response.meta['town_data']
        village_list = response.xpath('//tr[@class="villagetr"]')
        for village_node in village_list:
            village_data = dict(meta)
            number = village_node.xpath('td[1]/text()').extract()
            code = village_node.xpath('td[2]/text()').extract()
            name = village_node.xpath('td[3]/text()').extract()
            village_data['villageNumber'] = number[0]
            village_data['villageCode'] = code[0]
            village_data['villageName'] = name[0]
            yield village_data
