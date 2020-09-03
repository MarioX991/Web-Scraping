#import scrapy
from scrapy import Spider
# modules that have to be import to establish connection with theitam.py file
from scrapy.loader import ItemLoader #he merge items that pipe with the spider or hold that pipe

#fatch file from item.py
from  scrapy_first.items import QuotesSpiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        l = ItemLoader(item=QuotesSpiderItem(),response=response)

        #H1 tag from the page
        h1_tag = response.xpath('//h1/a/text()').extract_first() 
        # extrack all the tags that have been posisioned on the right are of the web page 
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract() 

        l.add_value("h1_tag",h1_tag)
        l.add_value("tags",tags)

        return l.load_item()


        # if we want to use folder item.py  this are steps:
        # 1. delete yield line 
        # 2. at the file item.py in section pass we transferr tags form above
        # and for every of them we add exra itam as scrapy.Filds()
        # 3.  we came beck here and import two modules 
        #      3.1 ItemLoader
        #      3.2 class that espablish connection with item.py folder
        # we add loadItem in our code adn call tham with l.add_values()

        # yield {"H1 tag": h1,"Tags": tag}









