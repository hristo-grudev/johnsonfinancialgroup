import scrapy


class JohnsonfinancialgroupItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
