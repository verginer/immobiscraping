import scrapy
from immobiliareIt.items import ImmobiliareitItem
import re

cleanUnicodePrice = re.compile("\D*(\d+\.\d+)\.*")


# http://www.immobiliare.it/Lucca/case_in_vendita-Lucca.html?criterio=rilevanza&pag=1
BASEQUERYPATH = "http://www.casa.it/vendita-residenziale/in-mi%2c+lombardia/lista-"
startUrls = [BASEQUERYPATH+str(pageNumber) for pageNumber in range(1, 2)]


class ImmobiliareSpider(scrapy.Spider):
	name = "casait"
	allowed_domains = ["casa.it"]
	start_urls = startUrls

	def parse(self, response):
		for href in response.xpath('//a[@rel="listingName"]/@href').extract():
			url = response.urljoin(href)
			print(url)
			yield scrapy.Request(url, callback=self.parse_listing_contents)

	def parse_listing_contents(self, response):
		item = ImmobiliareitItem()
		item['listingID'] = response.xpath('//p[@class="agencyId"]/text()').extract() 
		item['area'] = response.xpath('//li[@class="property_info"]//li[@class="first"]/span/text()').extract()
		item['bathrooms'] = response.xpath('//div[@class="featureList"]//li[contains(text(),"Bagni")]/span/text()').extract()
		item['gardenQ'] = response.xpath('//div[@class="featureList"]//li[contains(text(),"Giardino")]/span/text()').extract() 
		item['description'] = response.xpath('//meta[@itemprop="description"]/@content').extract() 
		item['address'] = response.xpath('//li[@class="address"]/h1/text()').extract() 
		item['price'] = response.xpath('//li[@class="price"]/span[@class="hidden"]/text()').extract() 
		item['url'] = response.url
		item['rooms'] = response.xpath('//div[@class="featureList"]//li[contains(text(),"Locali")]/span/text()').extract()
		item['condition'] =response.xpath('//div[@class="featureList"]//li[contains(text(),"Condizioni")]/span/text()').extract() 
		item['constructionYear'] = response.xpath('//div[@class="featureList"]//li[contains(text(),"Anno di costruzione")]/span/text()').extract()
		item['agency'] = response.xpath('//div[@class="emailAgentInfo"]/a/img[@class="logo"]/@alt').extract()
		item['propertyType'] = response.xpath('//li[@class="property_info"]//li[@class="type"]//text()').extract()

		yield item
