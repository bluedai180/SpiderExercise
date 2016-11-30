import scrapy

from exercise.items import ExerciseItem


class DmozSpider(scrapy.Spider):
    name = "exercise"
    allowed_domains = ["jirou.com"]
    start_urls = [
        "http://www.jirou.com/"
    ]

    def parse(self, response):
        sites = response.xpath('//div[@class="content6"]')
        items = []
        for site in sites:
            item = ExerciseItem()
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()

            item['title'] = [t.encode('utf-8') for t in title]
            item['link'] = [l.encode('utf-8') for l in link]

            items.append(item)
        return items