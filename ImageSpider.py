import scrapy

class ImageSpider(scrapy.Spider):
    name = 'imageSpider'
    start_url = ['']

    def parse(self, response):
        pass
