import scrapy


class EdgarSpider(scrapy.Spider):
    name = "edgar"

    start_urls = [
        'http://localhost:5000/companies/',
    ]

    def parse(self, response):
        # Follow every company link in the listing table
        for href in response.css('table.table a::attr(href)'):
            yield response.follow(href, self.parse_company)
        next_page = response.css('ul.pagination li.next:not(.disabled) a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_company(self, response):
        yield {}
