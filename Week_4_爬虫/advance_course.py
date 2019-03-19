# -*- coding:utf-8 -*-

'''
该爬虫用于练习页面跟随，
爬取实验楼某一课程的晋阶课程
'''

import scrapy


class  CourseFollowSpider(scrapy.Spider):

    name = "course_follow"
    start_urls = ["https://shiyanlou.com/courses/1"]

    def parse(self, response):

        course = {
                'name':response.xpath('//h4[@class="course-infobox-title"]/span[1]/text()').extract_first(),
                'author':response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
                }
        course = str(course)
        yield course

        filename = './course_follow_1.txt'
        with open(filename, 'a+') as f:
            f.write(course)
            f.write('\n')
            f.close()
        
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href').extract():
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse)
            # 打一个log获取相关url信息
            self.log("url:{}".format(response.urljoin(url)))
