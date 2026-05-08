from dataclasses import dataclass, asdict


@dataclass
class ScrapedItem:
    title: str
    url: str
    price: str | None = None
    description: str | None = None

    def to_dict(self):
        return asdict(self)