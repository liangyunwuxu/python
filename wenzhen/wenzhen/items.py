# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class WenzhenItem(Item):
    # define the fields for your item here like:
    pass


#xywy.com
class XywyItem(Item):
    link = Field()
    # pass

#haodf.com
class HaodfItem(Item):
    title = Field()
    url = Field()