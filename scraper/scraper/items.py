# -*- coding: utf-8 -*-
"""Items are containers to load with data."""
import scrapy

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


class ScraperItem(scrapy.Item):
    """Used to save all images via media pipeline."""

    file_urls = scrapy.Field()
    files = scrapy.Field()
