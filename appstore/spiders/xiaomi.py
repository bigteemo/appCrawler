# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from appstore.items import AppstoreItem


class XiaomiSpider(scrapy.Spider):
    name = "xiaomi"
    allowed_domains = ["app.mi.com"]
    start_urls = (
        'http://app.mi.com/',
    )

    def parse(self, response):
        sel = Selector(response)
        toplist = []
        apps = sel.xpath('//ul[@class="ranklist"]/li')

        for app in apps:
            item = AppstoreItem()
            item['rank'] =  app.xpath('div/h3/span/text()').extract()[0]
            item['name'] = app.xpath('div/h3/a[@class="hd"]/text()').extract()[0]
            item['category'] = app.xpath('div/div[@class="intro"]/a[@class="intro-category"]/text()').extract()[0]
            item['size'] = app.xpath('div/div[@class="intro"]/p/text()').extract()[0]

            #process size so that the "大小" character is removed
            item['size'] = item['size'].split(u'\uff1a')[1]
            toplist.append(item)

        return toplist
