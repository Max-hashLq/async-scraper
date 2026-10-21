Async Scraper

An asynchronous web scraping project built with Python. The scraper collects data from web pages and exports the results to JSON and CSV files.

Features

Asynchronous scraping with asyncio

Browser automation with Playwright

HTML parsing with BeautifulSoup

Pagination support

User-Agent rotation

JSON and CSV export

Logging and exception handling

Modular project structure

Tech Stack

Python

asyncio

Playwright

BeautifulSoup

JSON

CSV

Project Structure

async-scraper/
├── scraper/
│   ├── scraper.py
│   ├── exporter.py
│   └── logger.py
├── main.py
├── requirements.txt
└── README.md

Installation

Clone the repository:

git clone https://github.com/Max-hashLq/async-scraper.git
cd async-scraper

Create a virtual environment:

python -m venv .venv

Activate it on Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Activate it on Linux or macOS:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

Run the scraper:

python main.py

The collected data is exported to JSON and CSV files.

Notes

Make sure you have permission to scrape the target website and follow its terms of service.

Author

Max-hashLq

GitHub: https://github.com/Max-hashLq
