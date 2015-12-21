# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector

from wenzhen.items import XywyItem


class XywytwoSpider(Spider):
    name = "xywy_bak"
    allowed_domains = ["xywy.com"]
    start_urls = [
        'http://club.xywy.com/list_645_all_11.htm',
    ]

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//table[@class="f12 kstable"]')
        # return links
        items = []
        for link in links:
            item = XywyItem()
            item['link'] = link.xpath('tr/td/a[2]/@href').extract()
            items.append(item)
        return items
