from basespider import BaseSpider

from content import Content


class RedditSpider(BaseSpider):
    name = 'redditspider'
    start_urls = ['https://www.reddit.com/r/programming/top/?sort=top&t=day',
                  'https://www.reddit.com/r/programming/top/?sort=top&t=week']
    content_found = []

    def parse(self, response):
        for entry in response.css('div.thing'):
            title = entry.css("p.title > a::text").extract_first()
            # comments_url = entry.css(TODO).extract_first()
            url = entry.css("p.title > a::attr(href)").extract_first()
            score = entry.css(".score.unvoted::text").extract_first()
            if score == "•":
                score = None
            else:
                score = int(score)

            content = Content(source="reddit", title=title, url=url, score=score)
            self.content_found.append(content)
