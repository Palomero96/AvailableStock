import requests
from datetime import date
from bs4 import BeautifulSoup

__default_header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
parser='html.parser'

#Scrap the page to check if it is available
def check_pccomponentes(url):
	# Getting the page
	page = requests.get(url, headers=__default_header)
	# Creating BeautifulSoup Object
	soup = BeautifulSoup(page.content, parser)

	allbuttons = soup.find_all("button", {"class": "buy-button"})
	if not allbuttons:
		#Return False if not available
		return False
	#Loop buttons to check if it is available
	for button in allbuttons:
		if "Comprar" in button.findChild().text:
			return True
	
	return False
