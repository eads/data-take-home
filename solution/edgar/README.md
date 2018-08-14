# Homework solution: Scraper

We strongly recommend creating a virtualenv before performing the steps below.

Edgar must be running locally.

## Prerequisites

* Python 3

## Install requirements

`pip install -r requirements.txt`

# Run the scraper

```
scrapy crawl -o edgar.json edgar
```

Scraped data will now be available in `edgar.json`.

# Run tests

```
pytest
```
