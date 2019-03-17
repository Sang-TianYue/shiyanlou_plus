# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):  # 继承自scrapy.Item
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 需要爬取的数据定义在此
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()
