# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class FitnessItem(Item):
    muscle_id = Field()
    name = Field()
    difficulty_name = Field()
    training_points = Field()
    category_name = Field()
    muscle_name = Field()
    equipments = Field()
    description = Field()
    video = Field()
    gif = Field()
    muscle_pic = Field()
    muscle_front_img = Field()
    muscle_back_img = Field()
    other_muscles = Field()
    file_urls = Field()
    files = Field()
