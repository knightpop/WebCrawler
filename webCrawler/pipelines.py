from urllib import request
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        for image in item['imageURL']:
            request.urlretrieve(image, 'images/{}'.format(image.split('/')[-1]))
        return item
