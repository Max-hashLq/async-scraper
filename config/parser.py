from bs4 import BeautifulSoup

def parse_items(html: str):
    soup = BeautifulSoup(html, "html.parser")
    items = []

    # более стабильный селектор hh.ru
    cards = soup.select("div[data-qa='vacancy-serp__vacancy']")

    for card in cards:
        title_el = card.select_one("a[data-qa='serp-item__title']")
        company_el = card.select_one("[data-qa='vacancy-serp__vacancy-employer']")
        salary_el = card.select_one("[data-qa='vacancy-serp__vacancy-compensation']")
        link_el = title_el

        if not title_el:
            continue

        items.append({
            "title": title_el.get_text(strip=True),
            "company": company_el.get_text(strip=True) if company_el else None,
            "salary": salary_el.get_text(strip=True) if salary_el else "Not specified",
            "url": link_el["href"] if link_el else None
        })

    return items