# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import codecs
import json


class ExercisePipeline(object):

    def __init__(self):
        self.file = codecs.open('jirou_data_utf8.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item) + '\n')
        self.file.write(line)
        return item
