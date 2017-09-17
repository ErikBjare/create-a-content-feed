import logging

import scrapy
# from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
logging.getLogger().setLevel(logging.WARNING)

from content import Content

# Here we import the spiders
# To understand them, read the scrapy docs.
# This is a good start: https://doc.scrapy.org/en/latest/topics/practices.html
from redditspider import RedditSpider
from hnspider import HNSpider

SETTINGS = {
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
}

# Clean last result
open("content.json", "w+").close()

crawler = CrawlerProcess(SETTINGS)

logging.getLogger("scrapy.middleware").setLevel(logging.WARNING)
logging.getLogger("scrapy.statscollectors").setLevel(logging.WARNING)
logging.getLogger("scrapy.core.engine").setLevel(logging.WARNING)

crawler.crawl(RedditSpider)
crawler.crawl(HNSpider)
crawler.start()
