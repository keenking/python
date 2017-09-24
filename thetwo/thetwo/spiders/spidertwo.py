# -*- coding: utf-8 -*-
import scrapy
from thetwo.items import ThetwoItem
import os

class SpidertwoSpider(scrapy.Spider):
    name = 'spidertwo'
    allowed_domains = ['http://www.stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/43.html']
    baseUrl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'

    def parse(self, response):
        city_list = response.xpath('//tr[@class="citytr"]')
        for city_node in city_list:
            city_data = ThetwoItem()
            number = city_node.xpath('td[1]/a/text()').extract()
            name = city_node.xpath('td[2]/a/text()').extract()
            city_url = city_node.xpath('td[1]/a/@href').extract()
            city_data['cityNumber'] = number[0]
            city_data['cityName'] = name[0]
            country_url = self.baseUrl + str(city_url[0])
            yield scrapy.Request(country_url, meta={'city_data': city_data}, callback=self.country_parse,
                                 encoding='utf-8', dont_filter=True, priority=1)

    def country_parse(self, response):
        country_list = response.xpath('//tr[@class="countytr"]')
        for country_node in country_list:
            country_data = response.meta['city_data']
            if country_node.xpath('td/a/text()'):   #此处if语句的判断耗时2小时，铭记。。
                number = country_node.xpath('td[1]/a/text()').extract()
                name = country_node.xpath('td[2]/a/text()').extract()
                country_data['countryNumber'] = number[0]
                country_data['countryName'] = name[0]
                country_url = country_node.xpath('td[1]/a/@href').extract()[0]
                country_data['countryUrlitem'] = country_url
                base_link = os.path.dirname(response.url)
                next_link = '/'.join([base_link, country_url])
                country_data['nextUrl'] = next_link
                print('************************'+'\n'+next_link+'\n'+'************************')
                # yield country_data
                yield scrapy.Request(next_link, meta={'country_data': country_data}, callback=self.town_parse,
                                     encoding='utf-8', dont_filter=True, priority=2)
            # else:
            #     number = country_node.xpath('td[1]/text()').extract()
            #     name = country_node.xpath('td[2]/text()').extract()
            #     country_data['countryNumber'] = number[0]
            #     country_data['countryName'] = name[0]
            #     yield country_data
    def town_parse(self, response):
        town_list = response.xpath('//tr[@class="towntr"]')
        for town_node in town_list:
            town_data = response.meta['country_data']
            number = town_node.xpath('td[1]/a/text()').extract()
            name = town_node.xpath('td[2]/a/text()').extract()
            town_data['townNumber'] = number[0]
            town_data['townName'] = name[0]
            yield town_data



