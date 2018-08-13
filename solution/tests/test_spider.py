"""
These tests rely on the Edgar test server running locally.

In an ideal world, we'd use something like Betamax to record the
session. But since Edgar is run locally, it's easy enough to
require it for basic tests.
"""
import requests

from edgarscraper.spiders.edgar import EdgarSpider
from scrapy.http import HtmlResponse


def test_listing():
    spider = EdgarSpider()
    response = requests.get('http://localhost:5000/companies/?page=10')
    scrapyresponse = HtmlResponse(url=response.url, body=response.content, request=response.request)
    data = list(spider.parse(scrapyresponse))
    assert data[4].url == 'http://localhost:5000/companies/Schmidt%20Inc'
