import scrapy

class ImageSpider(scrapy.Spider):
    name = 'imageSpider'
    # start_url = ['']
    start_urls = ['http://web.humoruniv.com/board/humor/read.html?table=wphoto&number=104474']

    def parse(self, response):
        print('Parsing')
        print(response.css('div#wrap_img a::attr(href)').extract())