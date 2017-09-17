from basespiders import ContentSpider

from content import Content


class HNSpider(ContentSpider):
    name = 'hnspider'

    # Only check the first two pages
    start_urls = ['https://news.ycombinator.com/news?p=' + str(i)
                  for i in range(0, 3)]

    def parse(self, response):
        # TODO: Might want to use RSS feed instead
        items = []

        # HN has a weird table account:
        #  - Every (n*3)th line is a title
        #  - Every (n*3+1)th line is a subtitle (that contains the score)
        entries = response.css('table.itemlist > tr')
        for i in range(0, len(entries), 3):
            # Extract the title
            title = entries[i + 0].css("td.title > a::text").extract_first()
            if title is None:
                # FIXME: Prevent this from happening in the first place
                # Something went wrong, skip
                continue

            # Extract the URL to the submission
            url = entries[i + 0].css("td.title > a::attr(href)").extract_first()

            # Extract the score of the post
            score = entries[i + 1].css("td > span.score::text").extract_first()
            if score:
                score = int(score.split()[0])

            content = Content(source="hn", title=title, url=url, score=score)

            items.append(content)

        self.save_many(items)
