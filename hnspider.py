from basespider import BaseSpider

from content import Content


class HNSpider(BaseSpider):
    # TODO: Might want to use RSS feed instead

    name = 'hnspider'

    # Only check the first two pages
    start_urls = ['https://news.ycombinator.com/news?p=1',
                  'https://news.ycombinator.com/news?p=2']

    content_found = list()

    def parse(self, response):
        entries = response.css('table.itemlist > tr')
        for i in range(0, len(entries), 3):
            title = entries[i + 0].css("td.title > a::text").extract_first()
            if title is None:
                # Something went wrong, skip
                # FIXME: Prevent this from happening in the first place
                continue
            url = entries[i + 0].css("td.title > a::attr(href)").extract_first()
            score = entries[i + 1].css("td > span.score::text").extract_first()
            if score:
                score = score.split()[0]
            content = Content(source="hn", title=title, url=url, score=score)
            # print(content)
            self.content_found.append(content)
