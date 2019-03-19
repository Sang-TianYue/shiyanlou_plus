# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    #allowed_domains = ['github.com']
    start_urls = ['http://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for i in response.css('li.col-12'):
            item = GithubItem({
                'name':i.css('h3 a::text').re_first('\s+(.+)'),
                'update_time':i.css('div div relative-time::attr(datetime)').extract_first()
                })
            yield item

        next_page = response.css("div.paginate-container div a[href*='after']::attr(href)").re_first('.+=(.+)&.+')
        if next_page is not None:
            next_page = 'https://github.com/shiyanlou?after='+next_page+'&tab=repositories'
            yield scrapy.Request(url=next_page, callback=self.parse)

