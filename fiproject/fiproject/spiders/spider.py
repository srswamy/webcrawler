import urlparse
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider
BASE_URL = 'http://scrapy.org'

class Spyder(Spider):
    name = 'spyderman'
    allowed_domains = ['scrapy.org']
    start_urls = ['http://scrapy.org/companies', 'http://scrapy.org/community']

def parse(self, response):
    selection = Selector(response)
    requests = []
    for href in selection.xpath('//ul/li/a'):
        name = href.xpath('text()')[0].extract().strip()
	link = href.xpath('@href')[0].extract().strip()
	requests.append(Request(link = urlparse.urljoin(BASE_URL, link), callback=parse_subcategory))
	return requests

def parse_items(self, response):
    selection = Selector(response)
    requests = []

    name = selection.xpath('//p/text()')[0].extract().strip()
    url = selection.xpath('//a/@href')[0].extract().strip()

    item = FiprojectItem(url, name)

    return [item]
