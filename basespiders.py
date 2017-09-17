import json
import threading

import scrapy

from content import Content


def load_content():
    with open("content.json", "r") as f:
        contentlist = json.load(f)
    return [Content(**c_dict) for c_dict in contentlist]


file_lock = threading.Lock()


def save_many(items):
    with file_lock:
        with open("content.json", "r") as f:
            data = f.read()

        data = json.loads(data) if data else []
        data.extend([item.to_dict() for item in items])

        with open("content.json", "w+") as f:
            json.dump(data, f)


class ContentSpider(scrapy.Spider):
    custom_settings = {
        'EXTENSIONS': {
            # 'scrapy.extensions.corestats.CoreStats': None,
            # 'scrapy.extensions.logstats.LogStats': None,
            'scrapy.extensions.telnet.TelnetConsole': None,
        }
    }

    def save_many(self, items):
        save_many(items)
