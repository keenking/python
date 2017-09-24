# -*- coding: utf-8 -*-
import scrapy
from home_scrapy.items import HomeScrapyItem


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
        for city_node in city_list:
            city_data = response.meta['province_data']
            number = city_node.xpath('td[1]/a/text()').extract()
            name = city_node.xpath('td[2]/a/text()').extract()
            city_url = city_node.xpath('td[1]/a/@href').extract()
            city_data['cityNumber'] = number[0]
            city_data['cityName'] = name[0]
            country_url = self.baseUrl + str(city_url[0])
            # yield city_data
            yield scrapy.Request(country_url, meta={'city_data': city_data}, callback=self.country_parse,
                                 encoding='utf-8', dont_filter=True)
            # 县

    def country_parse(self, response):
        country_list = response.xpath('//tr[@class="countytr"]')
        # response.xpath('//tr[@class="countytr"]/td/text()').extract()
        for country_node in country_list:
            country_data = response.meta['city_data']
            if not country_node.xpath('td/text()'):
                number = country_node.xpath('td[1]/a/text()').extract()
                name = country_node.xpath('td[2]/a/text()').extract()
                country_data['countryNumber'] = number[0]
                country_data['countryName'] = name[0]
                yield country_data
            else:
                number = country_node.xpath('td[1]/text()').extract()
                name = country_node.xpath('td[2]/text()').extract()
                country_data['countryNumber'] = number[0]
                country_data['countryName'] = name[0]
                yield country_data

            # # else:
            #     number = country_node.xpath('td[1]/a/text()').extract()
            #     name = country_node.xpath('td[2]/a/text()').extract()
            #     country_data['countryNumber'] = number[0]
            #     country_data['countryName'] = name[0]
            #     country_url = country_node.xpath('td[1]/a/@href').extract()
            #     a = str(number[0])[0:2]
            #     town_url = self.baseUrl + a + '/' +str(country_url[0])
            #     yield country_data
                # yield scrapy.Request(town_url, meta={'country_data': country_data}, callback=self.town_parse,
                #                      encoding='utf-8', dont_filter=True)
                # 乡

    # def town_parse(self, response):
    #     town_list = response.xpath('//tr[@class="towntr"]')
    #     for town_node in town_list:
    #         town_data = response.meta['country_data']
    #         number = town_node.xpath('td[1]/a/text()').extract()
    #         name = town_node.xpath('td[2]/a/text()').extract()
    #         town_url = town_node.xpath('td[1]/a/@href').extract()
    #         town_data['townNumber'] = number[0]
    #         town_data['townName'] = name[0]
    #         village_url = self.baseUrl + str(town_url[0])
    #         yield town_data
