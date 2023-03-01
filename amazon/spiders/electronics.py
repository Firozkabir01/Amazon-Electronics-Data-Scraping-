import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ElectronicsSpider(CrawlSpider):
    name = "electronics"
    # allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/s?i=electronics-intl-ship&rh=n%3A16225009011&fs=true&page=1&qid=1677663272&ref=sr_pg_1"
        ]
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h2/a'),
             callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]'),
             follow=True)
        )

    def parse_item(self, response):
        yield {
            'title': response.xpath('//span[@id="productTitle"]/text()').get().strip(),
            'reviews': response.xpath('//span[@id="acrCustomerReviewText"]/text()').get(),
            'ratings': response.xpath('(//span[@class="a-icon-alt"])[1]/text()').get(),
            'QA': response.xpath('//a[@id="askATFLink"]/span/text()').get()
        }