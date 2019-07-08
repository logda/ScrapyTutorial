import scrapy



class QuoteSpider(scrapy.Spider):
    name = 'quotes_aoke'
    start_urls = ['http://youmoguoji.com/main/home/cat?categoy=%E5%A9%B4%E5%84%BF%E5%A5%B6%E7%B2%89&page=1']

    def parse(self, response):

        output = response.css('div.product-name').extract()
        yield output