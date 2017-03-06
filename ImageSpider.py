import scrapy

class ImageSpider(scrapy.Spider):
    name = 'imageSpider'
    # start_url = ['']
    start_urls = ['http://web.humoruniv.com/board/humor/read.html?table=wphoto&number=104474']

    def parse(self, response):
        print(response.TextResponse.xpath('//img'))
## TODO response.css('div#wrap_img a::attr(href)').extract()이렇게 하면 되지 않을까?