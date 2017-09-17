from typing import Optional


class Content:
    def __init__(self, source=None, title=None, url=None,
                 score: Optional[int] = None) -> None:
        self.source = source
        self.title = title
        self.url = url
        self.score = score

    def __str__(self):
        return "[{}] {} ({})".format(self.score, self.title, self.url)

    def __repr__(self):
        title_maxlen = 40
        return "<Content source='{}' title='{}'>".format(
            self.source,
            (self.title[:title_maxlen] + ("..." if len(self.title) > title_maxlen else "")).encode("ascii", "ignore").decode("ascii")
        )

    def to_dict(self):
        return {
            "source": self.source,
            "title": self.title,
            "url": self.url,
            "score": self.score,
        }
