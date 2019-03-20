# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import MultipageCourseItem

class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    # allowed_domains = ['shiyanlou.com/courses']
    start_urls = ['http://shiyanlou.com/courses/']

    def parse(self, response):
        for course in response.css('a.course-box'):
            item = MultipageCourseItem()

            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract_first()
            item['image'] = course.xpath('.//div[@class="course-img"]/img/@src').extract_first()

            course_url = response.urljoin(course.xpath('@href').extract_first())
            request = scrapy.Request(course_url, callback=self.parse_author)
            request.meta['key'] = item
            yield request

    def parse_author(self, response):
        item = response.meta['key']
        item['author'] = response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()

        yield item
