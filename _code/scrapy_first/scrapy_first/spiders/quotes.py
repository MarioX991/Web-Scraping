import scrapy
import pandas as pd
import json 


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #H1 tag from the page
        h1_tag = response.xpath('//h1/a/text()').extract_first() 
        # extrack all the tags that have been posisioned on the right are of the web page 
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract() 

        # create a dict from all scraped elements from webpage
        dict = {"H1_tag" : h1_tag,
                "Tags":tags}
                # transform and save dict to the json file
        with open('data.json', 'w') as fp:
            json.dump(dict, fp)









