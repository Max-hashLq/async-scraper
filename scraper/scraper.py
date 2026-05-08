import asyncio
from playwright.async_api import Page
from config.settings import START_URL, TIMEOUT, PAGINATION_LIMIT
from scraper.browser import BrowserManager
from scraper.parser import parse_items, get_next_page_url
from scraper.utils import async_retry


class AsyncScraper:
    def __init__(self, logger):
        self.logger = logger
        self.browser_manager = BrowserManager(logger)
        self.results = []

    @async_retry()
    async def fetch_page_content(self, page: Page, url: str) -> str:
        self.logger.info("Opening page: %s", url)
        await page.goto(url, timeout=TIMEOUT, wait_until="domcontentloaded")
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(5000)
        return await page.content()

    async def scrape_page(self, page: Page, url: str) -> tuple[list, str | None]:
        html = await self.fetch_page_content(page, url)
        self.logger.info(html[:2000])
        items = parse_items(html)
        next_page = get_next_page_url(html)

        self.logger.info("Parsed %d items from %s", len(items), url)
        return items, next_page

    async def run(self):
        await self.browser_manager.start()

        context = await self.browser_manager.new_context()
        page = await context.new_page()

        current_url = START_URL
        current_page_num = 1

        try:
            while current_url and current_page_num <= PAGINATION_LIMIT:
                self.logger.info("Scraping pagination page %d", current_page_num)

                items, next_page = await self.scrape_page(page, current_url)
                self.results.extend(items)

                if not next_page:
                    self.logger.info("No next page found. Stopping pagination.")
                    break

                current_url = next_page
                current_page_num += 1

                await asyncio.sleep(1)

        finally:
            await context.close()
            await self.browser_manager.stop()

        return self.results