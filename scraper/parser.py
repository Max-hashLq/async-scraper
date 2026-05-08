from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config.settings import BASE_URL
from scraper.models import ScrapedItem


def parse_items(html: str) -> list[ScrapedItem]:
    soup = BeautifulSoup(html, "html.parser")
    items = []

    cards = soup.select(".item-card")

    for card in cards:
        title_el = card.select_one(".item-title")
        link_el = card.select_one("a")
        price_el = card.select_one(".item-price")
        desc_el = card.select_one(".item-description")

        if not title_el or not link_el:
            continue

        item = ScrapedItem(
            title=title_el.get_text(strip=True),
            url=urljoin(BASE_URL, link_el.get("href", "")),
            price=price_el.get_text(strip=True) if price_el else None,
            description=desc_el.get_text(strip=True) if desc_el else None,
        )
        items.append(item)

    return items


def get_next_page_url(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    next_btn = soup.select_one("a.next")

    if next_btn and next_btn.get("href"):
        return urljoin(BASE_URL, next_btn["href"])

    return None