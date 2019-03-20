# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseImageItem

class CourseImageSpider(scrapy.Spider):
    name = 'course_image'
    # allowed_domains = ['shiaynlou.com/courses']
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        item = CourseImageItem()
        item['image_urls'] = response.css('div.course-img img::attr(src)').extract()
        yield item
