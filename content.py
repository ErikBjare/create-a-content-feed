from typing import Optional


class Content:
    def __init__(self, source=None, title=None, url=None, score: Optional[int] = None):
        self.source = source
        self.title = title
        self.url = url
        self.score = score

    def __str__(self):
        return "[{}] {} ({})".format(self.score, self.title, self.url)
