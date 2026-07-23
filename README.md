# Web Scraping Practice

Practice repo for learning web scraping with Python — requests, BeautifulSoup, 
and pandas for cleaning/exporting scraped data.

## Tools used
- Python 3.14
- requests / httpx
- BeautifulSoup / selectolax
- pandas

## Exercises

| Folder | Site | What it covers |
|---|---|---|
| [01-countries-simple](./01-countries-simple) | scrapethissite.com | Single-page scrape, nested tags, CSV export |
| [02-hockey-multipage](./02-hockey-multipage) | scrapethissite.com | Multi-page loop, random delay, function-based scraper |

## Setup

\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
\`\`\`vi