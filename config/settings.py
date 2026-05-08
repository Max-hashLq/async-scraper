from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EXPORTS_DIR = BASE_DIR / "exports"
LOGS_DIR = BASE_DIR / "logs"

START_URL = "https://www.avito.ru/sankt-peterburg/kvartiry/prodam/do-6-mln-rubley-ASgBAgECAUSSA8YQAUXGmgwXeyJmcm9tIjowLCJ0byI6NjAwMDAwMH0?context=H4sIAAAAAAAA_wEmANn_YToxOntzOjE6InkiO3M6MTY6IlF0SjQwWTN4ODJmNW1HQloiO33qbt7UJgAAAA&f=ASgBAgECAkSSA8YQygiCWQFFxpoMF3siZnJvbSI6MCwidG8iOjYwMDAwMDB9&localPriority=0"
BASE_URL = "https://www.avito.ru"

HEADLESS = True
TIMEOUT = 30000
MAX_RETRIES = 3
RETRY_DELAY = 2

CONCURRENT_PAGES = 3

EXPORT_JSON = EXPORTS_DIR / "results.json"
EXPORT_CSV = EXPORTS_DIR / "results.csv"
LOG_FILE = LOGS_DIR / "scraper.log"

USER_AGENTS_ENABLED = True

PROXY = None
# Пример:
# PROXY = {
#     "server": "http://proxyhost:port",
#     "username": "user",
#     "password": "pass"
# }

PAGINATION_LIMIT = 5