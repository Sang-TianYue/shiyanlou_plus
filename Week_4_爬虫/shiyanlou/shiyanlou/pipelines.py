# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine


class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        '''
        经过parse处理的item被传到这里，
        这里的代码作用于每一个item对象
        这个方法必须要返回一个item对象
        '''
        item['students'] = int(item['students'])

        #self.session.add(Course(**item))
        # item = Course(
         #       name = item['name'],
          #      description = item['description'],
          #      type = item['type'],
           #     students = item['students']
            #    )
        #self.session.add(course)
        # 当课程人数少于1000时，不保存
        if item['students'] < 1000:
            raise DropItem('Course students less than 1000.')
        else:
            self.session.add(Course(**item))
        return item

    def open_spider(self, spider):
        '''
        当爬虫被开启的时候调用
        '''
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        '''
        当爬虫被关闭的时候调用
        '''
        self.session.commit()
        self.session.close()
