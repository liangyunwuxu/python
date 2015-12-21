# -*- coding: utf-8 -*-
from scrapy.spiders import Spider

class Xywy1Spider(Spider):
    name = "xywy_1"
    allowed_domains = ["xywy.com"]
    start_urls = (
        'http://club.xywy.com/list_679_all_11.htm',
    )
    def parse(self, response):
        open('xywy_link_1.txt','wb').write(response.body)

# if __name__ == '__main__':
#运行成功