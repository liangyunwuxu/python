# -*- coding: utf-8 -*-
from scrapy.spiders import Spider

from wenzhen.items import HaodfItem


class HaodfSpider(Spider):
    name = "haodf"
    allowed_domains = ["haodf.com"]
    start_urls = (
        'http://zixun.haodf.com/dispatched/all.htm?p=1',
    )

    def parse(self, response):
        items = []
        content = response.xpath('//li[@class="clearfix"]')
        for i in content:
            item = HaodfItem()
            item['title'] = i.xpath('span[1]/a[2]/text()').extract()
            item['url'] = i.xpath('span[1]/a[2]/@href').extract()
            items.append(item)
        return items

