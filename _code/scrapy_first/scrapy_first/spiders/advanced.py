import scrapy
import json 


class AdvancedSpider(scrapy.Spider):
    name = 'advanced'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # Grab every Box where has been written text  
        quotes = response.xpath('//*[@class="quote"]')

        # let's now iterate thought every elements(quote) in quotes
        for quote in quotes:
            #extract text form each box
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            # extract author of the extracted text
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            # extract tags from he current box
            tags = quote.xpath('.//*[@class="author"]/text()').extract_first()


            yield {'Text': text, 'Author': author, 'Tags': tags}



            # Now we want to iterate through pages on the website
            next_url_page = response.xpath('//*[@class = "next"]/a/@href').extract_first()
            # Grab absolute next page URL 
            absolute_next_page_url = response.urljoin(next_url_page)


            yield scrapy.Request(absolute_next_page_url)


            #create a dictionary who contain keywords as named element above 
            #dict = {'text': text, 'author': author, 'tags': tags}

        #with open('../../_data/file1.json', 'w') as fp:
           #json.dump(dict, fp)
