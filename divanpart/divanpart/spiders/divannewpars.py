from os import name

import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css("div.ProductCardMain_container__WXc_c")
        for svet in svets:
            yield {
                'name': svet.css('[itemprop="name"]::text').get(),
                'price': svet.css('[data-testid="price"]::text').get(),
                'url': svet.css('a').attrib['href'] }
