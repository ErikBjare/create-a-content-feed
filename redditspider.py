from basespiders import ContentSpider

from content import Content


class RedditSpider(ContentSpider):
    name = 'redditspider'
    start_urls = [
        'https://www.reddit.com/r/programming/top/?sort=top&t=day',
        # 'https://www.reddit.com/r/programming/top/?sort=top&t=week',
    ]

    def parse(self, response):
        items = []

        # Extract each row/item/"thing" in the reddit feed
        for entry in response.css('div.thing'):
            # Extract the title
            title = entry.css("p.title > a::text").extract_first()

            # Get the URL to the comments
            # comments_url = entry.css(TODO).extract_first()

            # Get the URL to the submission
            url = entry.css("p.title > a::attr(href)").extract_first()

            # Get the score of the post
            score = entry.css(".score.unvoted::text").extract_first()
            if score == "•":
                score = None
            else:
                score = int(score)

            content = Content(source="reddit", title=title, url=url, score=score)
            items.append(content)

        self.save_many(items)
