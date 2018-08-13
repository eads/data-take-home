"""
These tests rely on the Edgar test server running locally.

In an ideal world, we'd use something like Betamax to record the
session. But since Edgar is run locally, it's easy enough to
require it for basic tests.
"""
import requests

from edgarscraper.spiders.edgar import EdgarSpider
from scrapy.http import HtmlResponse

spider = EdgarSpider()


def get_scrapy_response(url):
    """
    Generate a scrapy response so we can test scraper methods directly.
    """
    response = requests.get(url)
    return HtmlResponse(url=response.url, body=response.content, request=response.request)


def test_parse_listing():
    """
    Parse a listing page. We expect Scrapy response objects with the correct
    URL.
    """
    response = get_scrapy_response('http://localhost:5000/companies/?page=10')
    listings = list(spider.parse(response))
    assert listings[4].url == 'http://localhost:5000/companies/Schmidt%20Inc'


def test_parse_company():
    """
    Parse a company page by comparing values from randomly chosen
    page to expected values.
    """
    response = get_scrapy_response('http://localhost:5000/companies/Watsica,%20Volkman%20and%20Rogahn')
    company = list(spider.parse_company(response))[0]

    assert {
        'name': 'Watsica, Volkman and Rogahn',
        'street_address': '448 Jamie Walk',
        'street_address_2': 'Suite 183',
        'city': 'Port Audie',
        'state': 'NorthCarolina',
        'zipcode': '48770',
        'phone_number': '+68(1)9163405663',
        'website': 'hermankemmer.info',
        'description': 'mesh value-added e-business'
    } == company
