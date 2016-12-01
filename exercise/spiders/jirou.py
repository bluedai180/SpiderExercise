import scrapy

from exercise.items import ExerciseItem


class DmozSpider(scrapy.Spider):
    name = "exercise"
    allowed_domains = ["hiyd.com"]
    start_urls = [
        "http://www.hiyd.com/play/course?id=38"
    ]

    def parse(self, response):
        sites = response.xpath('//div[@class="info"]')
        items = []
        for site in sites:
            item = ExerciseItem()
            title = site.xpath('span/text()').extract()
            #link = site.xpath('avatar/@href').extract()

            item['title'] = [t.encode('utf-8') for t in title]
            #item['link'] = [l.encode('utf-8') for l in link]

            items.append(item)
        return items