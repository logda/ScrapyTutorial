# -*- coding: utf-8 -*-
import scrapy


class AokeSpiderSpider(scrapy.Spider):
    name = 'aoke_spider'
    allowed_domains = ['http://youmoguoji.com/main/home/cat?categoy=%E5%A9%B4%E5%84%BF%E5%A5%B6%E7%B2%89']
    start_urls = ['http://http://youmoguoji.com/main/home/cat?categoy=%E5%A9%B4%E5%84%BF%E5%A5%B6%E7%B2%89/']

    def parse(self, response):
        output = response.css('div.product-name').extract
        yield output
