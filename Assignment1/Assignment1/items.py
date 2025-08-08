# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Assignment1Item(scrapy.Item):
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    book_availability = scrapy.Field()
    book_rating = scrapy.Field()
 

