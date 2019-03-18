# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem

class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']
    
    @property
    def start_urls(self):

        return ('https://www.shiyanlou.com/user/{}/'.format(i) for i in range(525000, 524800, -10))

    def parse(self, response):
        item = UserItem({
                    'name':response.css('div.userinfo-banner-details span.username::text').extract_first(),
                    'type':response.css('div.user-avatar a[href*="/vip"] img::attr(title)').extract_first(),
                    'level':response.css('div.userinfo-banner-details span.user-level::text').extract_first()[1:],
                    'join_date':response.css('div.userinfo-banner-details span.join-date::text').re_first(r'(.+)\W+'),
                    'status':response.css('div.userinfo-banner-details div.userinfo-banner-status span:nth-child(1)::text').extract_first(),
                    'school_job':response.css('div.userinfo-banner-details div.userinfo-banner-status span:nth-child(2)::text').extract_first(),
                    'learn_courses_num':response.css('a span.latest-learn-num::text').extract_first()
                    })
        yield item


