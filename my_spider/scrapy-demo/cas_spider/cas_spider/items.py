# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CasSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cas_href = scrapy.Field()
    cas = scrapy.Field()
    enname = scrapy.Field()
    as_enname = scrapy.Field()
    zhname = scrapy.Field()
    as_zhname = scrapy.Field()
