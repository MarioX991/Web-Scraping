# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyFirstPipeline:
    def process_item(self, item, spider):
        if item['h1_tag']:
            item['h1_tag'] = item['h1_tag'].upper()

        return item

#  if we use this pielines we ned to chance setting in settinns.py to turn on thi property 
# after that we just run our code(copy and paste name of the class into the settings file )