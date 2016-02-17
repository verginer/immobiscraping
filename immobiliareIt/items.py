# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImmobiliareitItem(scrapy.Item):
	listingID = scrapy.Field()
	listingDate = scrapy.Field()
	contract = scrapy.Field()
	area = scrapy.Field()
	bathrooms = scrapy.Field() 
	gardenQ = scrapy.Field()  
	energyClass = scrapy.Field()
	description = scrapy.Field()
	address = scrapy.Field() 
	price = scrapy.Field() 
	url = scrapy.Field()
	rooms = scrapy.Field()
	condition = scrapy.Field()
	constructionYear = scrapy.Field()
	agency = scrapy.Field()
	propertyType = scrapy.Field()

