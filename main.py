import asyncio
from scraper.logger import setup_logger
from scraper.scraper import AsyncScraper
from scraper.exporter import Exporter


async def main():
    logger = setup_logger()
    logger.info("Scraper started")

    scraper = AsyncScraper(logger)
    exporter = Exporter(logger)

    try:
        results = await scraper.run()
        items = [item.to_dict() for item in results]

        exporter.export_json(items)
        exporter.export_csv(items)

        logger.info("Scraping completed successfully. Total items: %d", len(items))
    except Exception as e:
        logger.exception("Scraper failed: %s", e)


if __name__ == "__main__":
    asyncio.run(main())