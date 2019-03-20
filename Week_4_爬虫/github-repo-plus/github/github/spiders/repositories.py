# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    #allowed_domains = ['github.com']
    start_urls = ['http://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for i in response.css('li.col-12'):
            item = GithubItem()

            item['name'] = i.css('h3 a::text').re_first('\s+(.+)')
            item['update_time'] = i.css('div div relative-time::attr(datetime)').extract_first()

            repo_url = i.css('h3 a::attr(href)').extract_first()
            repo_url = response.urljoin(repo_url)
            self.log('url:{}'.format(repo_url))
            request = scrapy.Request(repo_url, callback=self.parse_detail)
            request.meta['key'] = item

            yield request

        next_page = response.css("div.paginate-container div a[href*='after']::attr(href)").re_first('.+=(.+)&.+')
        if next_page is not None:
            next_page = 'https://github.com/shiyanlou?after='+next_page+'&tab=repositories'
            yield scrapy.Request(url=next_page, callback=self.parse)


    def parse_detail(self, response):
        item = response.meta['key']
        item['commits'] = response.xpath('//ul[@class="numbers-summary"]/li[1]/a/span/text()').re_first('\s(\d+)\s')
        item['branches'] = response.xpath('//ul[@class="numbers-summary"]/li[2]/a/span/text()').re_first('\s(\d+)\s')
        item['releases'] = response.xpath('//ul[@class="numbers-summary"]/li[3]/a/span/text()').re_first('\s(\d+)\s')

        yield item

