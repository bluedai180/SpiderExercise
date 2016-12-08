import scrapy

from exercise.items import ExerciseItem


class DmozSpider(scrapy.Spider):
    name = "exercise"
    allowed_domains = ["hiyd.com"]
    start_urls = [
        "http://www.hiyd.com/play/course?id=38"
    ]

    def parse(self, response):
        #sites = response.xpath('//li[@class="action"]')
        items = []

        # for site in sites:
        #     item = ExerciseItem()
        #     print(site)
        #     title = site.xpath('//span[@class="name"]/text()').extract()
        #     link = site.xpath('//span[@class="avatar"]//@action-detail').extract()
        #
        #     item['title'] = [t for t in title]
        #     item['link'] = [l for l in link]
        #     items.append(item)

        item = ExerciseItem()
        item['title'] = response.xpath('//li[@class="action"]//span[@class="name"]/text()').extract()
        item['link'] = response.xpath('//li[@class="action"]//span[@class="avatar"]//@action-detail').extract()
        return item
