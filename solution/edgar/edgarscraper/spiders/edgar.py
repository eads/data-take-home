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

        def extract(query):
            """
            Pull text from links in table.
            """
            return response.css('%s::text' % query).extract_first().strip()

        yield {
            'name': extract('#name'),
            'street_address': extract('#street_address'),
            'street_address_2': extract('#street_address_2'),
            'city': extract('#city'),
            'state': extract('#state'),
            'zipcode': extract('#zipcode'),
            'phone_number': extract('#phone_number'),
            'website': extract('#website'),
            'description': extract('#description'),
        }
