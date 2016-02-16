# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImmobiliareitItem(scrapy.Item):
	listingID = scrapy.Field() # response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "ferimento")]/following::td[1]/text()').extract()
	listingDate = scrapy.Field() # response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Data")]/following::td[1]/text()').extract()
	contract = scrapy.Field() # response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Contratto:")]/following::td[1]/text()').extract()
	area = scrapy.Field() # response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Superficie:")]/following::td[1]/text()').extract()
	bathrooms = scrapy.Field() # response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Bagni:")]/following::td[1]/text()').extract()
	gardenQ = scrapy.Field()  # response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Giardino:")]/following::td[1]/text()').extract()
	energyClass = scrapy.Field()  # response.xpath('//img[@class="imgClasseEnergetica"]/@alt').extract()
	description = scrapy.Field()  # response.xpath('//div[@class="descrizione"]/text()').extract()
	address = scrapy.Field()  # [x.strip() for x in response.xpath('//div[contains(@class,"indirizzo_")]/text()').extract()]
	price = scrapy.Field()  # response.css('div.info_annuncio div.dettaglio_superficie strong::text').extract()
	url = scrapy.Field()
	# price re.match("\D*(\d+\.\d+)\.*",UNICODEPRICE).groups()