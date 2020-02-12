# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listing_id = scrapy.Field()
    title = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    neighborhood = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    max_occupancy = scrapy.Field()
    service_fee = scrapy.Field()


