import scrapy


class EdgarSpider(scrapy.Spider):
    name = "edgar"

    start_urls = [
        'http://localhost:5000/companies/',
    ]

    def parse(self, response):
        next_page = response.css('ul.pagination li.next:not(.disabled) a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
