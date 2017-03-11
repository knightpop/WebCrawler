import scrapy

from ..pictures import pictures

class ImageSpider(scrapy.Spider):
    name = 'humoruniv'
    # start_url = ['']
    start_urls = list(map(
        lambda pg: 'http://web.humoruniv.com/board/humor/list.html?table=wphoto&pg={}'.format(pg), range(127)))
    # start_urls = ['http://web.humoruniv.com/board/humor/list.html?table=wphoto&pg=0']

    def parse(self, response):
        picturePageURL = response.xpath('//div/table/tr/td/div[@id="item"]/a').css('a::attr(href)').extract()
        for picturePage in picturePageURL:
            yield scrapy.Request('http://web.humoruniv.com/board/humor/{}'.format(picturePage), callback=self.parse_image)

    def parse_image(self, response):
        images = response.css('div#wrap_img a::attr(href)').extract()
        return pictures(imageURL=images)



