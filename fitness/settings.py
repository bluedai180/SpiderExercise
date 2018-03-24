# Scrapy settings for exercise project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'fitness'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['fitness.spiders']
NEWSPIDER_MODULE = 'fitness.spiders'
# USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
ITEM_PIPELINES = {
    'fitness.pipelines.VideoPipeline': 1,
    'fitness.pipelines.MongoPipeline': 2
}
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "fitness"
MONGO_COLL = "info"
FILES_STORE = 'E:\worktest\SpiderExercise'
