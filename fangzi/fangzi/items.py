# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangziItem(scrapy.Item):

    house_img = scrapy.Field()
    house_href = scrapy.Field()
    house_title = scrapy.Field()
    house_desc = scrapy.Field()
    house_price = scrapy.Field()
    singel_price = scrapy.Field()
    house_time = scrapy.Field()
    house_detail = scrapy.Field()
    district = scrapy.Field()
    zone_href = scrapy.Field()
    s_cate = scrapy.Field()
    s_cate_href = scrapy.Field()
