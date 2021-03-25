import scrapy

from scrapy.loader import ItemLoader

from ..items import JohnsonfinancialgroupItem
from itemloaders.processors import TakeFirst


class JohnsonfinancialgroupSpider(scrapy.Spider):
	name = 'johnsonfinancialgroup'
	start_urls = ['https://www.johnsonfinancialgroup.com/about-us/news-events/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="card card-hover text-center hover"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="content"]//text()[normalize-space()]|//main//p//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=JohnsonfinancialgroupItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
