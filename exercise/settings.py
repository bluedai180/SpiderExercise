# Scrapy settings for exercise project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'exercise'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['exercise.spiders']
NEWSPIDER_MODULE = 'exercise.spiders'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
ITEM_PIPELINES = {
    'exercise.pipelines.ExercisePipeline': 300
}

