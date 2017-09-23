# -*- coding: utf-8 -*-
import scrapy
from home_scrapy.items import HomeScrapyItem


class SpideroneSpider(scrapy.Spider):
    name = 'spiderone'
    allowed_domains = ['http://www.stats.gov.cn']
    baseUrl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html']

    def parse(self, response):
        node_list = response.xpath('//tr[@class="provincetr"]/td/a')
        for province_node in node_list:
            province_data = HomeScrapyItem()
            name = province_node.xpath('text()').extract()
            url = province_node.xpath('@href').extract()
            province_data['provinceName'] = name[0]
            city_url = self.baseUrl + str(url[0])
            print(city_url)
            yield scrapy.Request(city_url, meta={'province_data': province_data}, callback=self.city_parse, encoding='utf-8', dont_filter=True)
    def city_parse(self,response):
        city_list = response.xpath('//tr[@class="citytr"]')
        print('-----------')
        for city_node in city_list:
            city_data = response.meta['province_data']
            name1 = city_node.xpath('td[1]/a/text()').extract()
            name2 = city_node.xpath('td[2]/a/text()').extract()
            city_url = city_node.xpath('td[1]/a/@href').extract()
            city_data['planNumber'] = name1[0]
            city_data['cityName'] = name2[0]
            country_url = self.baseUrl + str(city_url[0])
            yield city_data







