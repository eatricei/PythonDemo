# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_auther = scrapy.Field()
    book_pub = scrapy.Field()
    book_publication_date = scrapy.Field()
    book_price = scrapy.Field()
    book_sort = scrapy.Field()
    book_status = scrapy.Field()
    book_id = scrapy.Field()
