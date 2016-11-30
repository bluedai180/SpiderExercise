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
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPLINES = {'jirou_data_utf8.json' : 300}

