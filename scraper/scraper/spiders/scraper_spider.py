"""Example spider, gets everything within domain constraint."""
import os

import scrapy

from scraper.items import ScraperItem


class PyChallengeSpider(scrapy.Spider):
    """Example spider."""

    name = "pychallenge"
    # Selected because there aren't insane amounts of links -
    # thus easy to verify and test.
    allowed_domains = ["pythonchallenge.com"]
    start_urls = ["http://www.pythonchallenge.com"]

    def parse(self, response):
        """Called with Response object of each crawl URL."""
        for href in response.xpath('//@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.save_page)

    def save_page(self, response):
        """Write the page and assets to local storage."""
        file = response.url.split("/")[-1]
        filename = os.path.join('/home/vagrant/sync/scraper/files', file)
        with open(filename, 'wb') as f:
            f.write(response.body)

        item = ScraperItem()
        file_urls = response.xpath('//img/@src').extract()
        item['file_urls'] = [self.process_url(url) for url in file_urls]
        yield item

    def process_url(self, url):
        """Create correct url scheme to enable img download."""
        if url.startswith('http'):
            pass
        elif url.startswith('/'):
            url = 'http://www.pythonchallenge.com' + url
        else:
            url = 'http://www.pythonchallenge.com/' + url
        return url
