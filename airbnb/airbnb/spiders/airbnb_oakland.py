# -*- coding: utf-8 -*-
import scrapy


class AirbnbOaklandSpider(scrapy.Spider):
    name = 'airbnb_oakland'
    allowed_domains = ['www.airbnb.com']
    start_urls = ['http://www.airbnb.com/']

    def parse(self, response):
        pass
