# -*- coding: utf-8 -*-
from scrapy.spiders import Spider#,Rule
# from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector

from wenzhen.items import XywyItem


class XywytwoSpider(Spider):
    name = "xywy"
    allowed_domains = ["xywy.com"]
    start_urls = (
        'http://club.xywy.com/list_640_all_1.htm',
    )
    # rules = Rule(LinkExtractor(allow=r'club.xywy.com/list_645_all_[\d]{2}.html',),'parse_item',follow=True)
    # def parse(self, response):
    #     sel = Selector(response)
    #     links = sel.xpath('//table[@class="f12 kstable"]')
    #     # return links
    #     items = []
    #     for link in links:
    #         item = XywyItem()
    #         item['link'] = link.xpath('tr/td/a[2]/@href').extract()
    #         items.append(item)
    #     return items
    #
    # def parse_item(self,response):
    #     sel = Selector(response)
    #     links = sel.xpath('//a[@class="wu"][3]/@href')
    #     # links = sel.xpath('/html/body/div[6]/div[1]/div[4]/div/a[8]')
    #     for link in links:
    #         item = XywyItem()
    #         item['link'] = link.xpath('tr/td/a[2]/@href').extract()
    #         yield item
    def parse_next_url(self,response):
        sel = Selector(response)
        #获取下一页链接
        items = []
        links = sel.xpath('//table[@class="f12 kstable"]')
        for link in links:
            item = XywyItem()
            item['link'] = link.xpath('tr/td/a[2]/@href').extract()
            items.append(item)
        yield items

        #获得下一篇文章的url
        rel_url = sel.xpath('//a[@class="wu"][2]/@href').extract()
        next_url = 'http://club.xywy.com' + rel_url
        print next_url
        yield Request(next_url,callback=self.parse_next_url)