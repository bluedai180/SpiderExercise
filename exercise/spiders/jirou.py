import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.nzjsw.com"]
    start_urls = [
        "http://www.nzjsw.com/tuijian/duanlian/yaobu.html"
    ]

    def parse(self, response):
        filename = 'jirou.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        title = response.xpath('//title/text()').extract()
        print(title)