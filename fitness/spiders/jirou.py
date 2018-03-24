import json

import scrapy

from fitness.items import FitnessItem


class DmozSpider(scrapy.Spider):
    name = "fitness"
    allowed_domains = ["hiyd.com"]
    start_urls = [
        "http://www.hiyd.com/dongzuo"
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="cont"]/a[@target="_blank"]/@href').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_info)
        next_page_url = response.xpath('//a[@rel="next"]/@href').extract_first()
        if next_page_url is not None and next_page_url != "/dongzuo/?page=2":
            yield scrapy.Request(response.urljoin(next_page_url))

    def parse_info(self, response):
        item = FitnessItem()
        text = response.xpath('//script').extract()[-1]
        data_text = text.split("e.init(")[1].split(");")[0]
        json_text = json.loads(data_text)
        other_muscle = json_text["otherMuscles"]
        temp = []
        if len(other_muscle) != 0:
            for x in other_muscle:
                temp.append(self.change_muscle_id(x["muscle_id"]))

        item['name'] = json_text["name"]
        item['difficulty_name'] = json_text["difficulty_name"]
        item['training_points'] = json_text["trainingPoints"]
        item['category_name'] = json_text["category_name"]
        item['muscle_name'] = json_text["muscle_name"]
        item['muscle_id'] = self.change_muscle_id(json_text["muscle_id"])
        item['other_muscles'] = ",".join(temp)
        item['equipments'] = ("徒手训练" if json_text["equipments"][0] is None else json_text["equipments"][0]["name"])
        item['description'] = json_text["description"]
        item['video'] = json_text["video_url"]
        item['gif'] = json_text["gif"]
        item['muscle_pic'] = json_text["muscle_pic"]
        item['muscle_front_img'] = json_text["muscle_front_img"]
        item['muscle_back_img'] = json_text["muscle_back_img"]
        item['file_urls'] = [json_text["video_url"]]
        yield item

    def change_muscle_id(self, muscle_id):
        unknown = ["27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37"]
        known = ["9", "21", "12", "19", "10", "16", "23", "20", "20", "16", "16"]
        if muscle_id in unknown:
            muscle_id = known[unknown.index(muscle_id)]
        return muscle_id
