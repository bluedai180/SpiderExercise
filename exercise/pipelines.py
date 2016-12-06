# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import codecs
import json


class ExercisePipeline(object):

    def __init__(self):
        self.file = open('jirou.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + '\n'
        for x in item["title"]:
            #line = json.dumps(dict(("title", x.decode('utf-8')))) + '\n'
            self.file.write("{ \"title\":\"%s\" },\n" % x.decode('utf-8'))

        return item
