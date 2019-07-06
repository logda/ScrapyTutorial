import scrapy
#from ..items import QuotetutorialItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    start_urls = [
        'https://www.weibo.com/?category=1760'
    ]

    def parse(self, response):

        info = response.xpath('//*[(@id = "PCD_pictext_i_v5")]//*[contains(concat( " ", @class, " " ), concat( " ", "S_txt1", " " ))]').extract()

        yield info
