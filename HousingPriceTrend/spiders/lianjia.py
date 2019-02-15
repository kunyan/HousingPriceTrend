# -*- coding: utf-8 -*-
import scrapy

from HousingPriceTrend.items import HousingpricetrendItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']

    def parse(self, response):
        houses = response.css('ul.sellListContent').css('li.LOGCLICKDATA')
        items = []

        for house in houses:
            item = HousingpricetrendItem()
            item['name'] = house.css(
                'div.title > a::text').extract_first().strip()
            item['price'] = house.css(
                'div.totalPrice > span::text').extract_first().strip()
            houseInfo = house.css(
                'div.address > div.houseInfo::text').extract()
            print(houseInfo)
            # item['community'] = house.css(
            #     'div.houseInfo > a::text').extract_first().strip()
            # item['constructionArea'] = house.css(
            #     'div.houseInfo > span::text').extract_first().strip()
            # item['position'] = house.css(
            #     'div.houseInfo > span::text').extract_first().strip()
            # items.append(item)

        # print(items)
        # return items
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
