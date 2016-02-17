import scrapy
from immobiliareIt.items import ImmobiliareitItem
import re

cleanUnicodePrice = re.compile("\D*(\d+\.\d+)\.*")


# http://www.immobiliare.it/Lucca/case_in_vendita-Lucca.html?criterio=rilevanza&pag=1
BASEQUERYPATH = "http://www.immobiliare.it/Bolzano/case_in_vendita-Bolzano.html?criterio=rilevanza&pag="
startUrls = [BASEQUERYPATH+str(pageNumber) for pageNumber in range(1, 311)]


class ImmobiliareSpider(scrapy.Spider):
	name = "immobib"
	allowed_domains = ["immobiliare.it"]
	start_urls = startUrls

	def parse(self, response):
		for href in response.css('div .annuncio_title strong a::attr(href)').extract():
			url = response.urljoin(href)
			yield scrapy.Request(url, callback=self.parse_listing_contents)

	def parse_listing_contents(self, response):
		item = ImmobiliareitItem()
		item['listingID'] = response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "ferimento")]/following::td[1]/text()').extract()
		item['listingDate'] = response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Data")]/following::td[1]/text()').extract()
		item['contract'] = response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Contratto:")]/following::td[1]/text()').extract()
		item['area'] =  response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Superficie:")]/following::td[1]/text()').extract()
		item['bathrooms'] = response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Bagni:")]/following::td[1]/text()').extract()
		item['rooms'] = response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Locali:")]/following::td[1]/text()').extract()
		item['gardenQ'] = response.xpath('//div[@id="details"]/table//tr/td[contains(text(), "Giardino:")]/following::td[1]/text()').extract()
		item['energyClass'] = response.xpath('//img[@class="imgClasseEnergetica"]/@alt').extract()
		item['description'] = response.xpath('//div[@class="descrizione"]/text()').extract()[0].replace("\n","").replace("\t","")
		item['address'] = [x.strip() for x in response.xpath('//div[contains(@class,"indirizzo_")]/text()').extract()]
		item['price'] =  cleanUnicodePrice.match(response.css('div.info_annuncio div.dettaglio_superficie strong::text').extract()[0]).groups()
		item['url'] = response.url
		item['agency'] = response.xpath('//td[@class="infoCell"]//a/@href').extract()
		yield item
