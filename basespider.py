import scrapy


class BaseSpider(scrapy.Spider):
    custom_settings = {
        'EXTENSIONS': {
            'scrapy.extensions.corestats.CoreStats': None,
            'scrapy.extensions.logstats.LogStats': None,
            'scrapy.extensions.telnet.TelnetConsole': None,
        }
    }
