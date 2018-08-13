import scrapy


class EdgarSpider(scrapy.Spider):
    """
    Extract company data from a local instance of Edgar.

    This spider pages through the listings and follows each company link.
    """

    name = "edgar"

    start_urls = [
        'http://localhost:5000/companies/',
    ]

    def parse(self, response):
        # Follow every company link in the listing table
        for href in response.css('table.table a::attr(href)'):
            yield response.follow(href, self.parse_company)

        # Use "next" button to reliably find next listing page.
        next_page = response.css('ul.pagination li.next:not(.disabled) a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_company(self, response):
        yield {}
