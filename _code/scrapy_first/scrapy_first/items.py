# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyFirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    # we have transferred element s from the main page
    # and for every element we add 
    h1_tag  = scrapy.Field()
    tags =  scrapy.Field()
    #
