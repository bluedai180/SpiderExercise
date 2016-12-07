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
            print(title)
            link = site.xpath('avatar/@href').extract()
            item['title'] = [t for t in title]
            #item['link'] = [l for l in link]

            items.append(item)
        print(items)
        return items
