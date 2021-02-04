import requests
from datetime import date
from bs4 import BeautifulSoup

__default_header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

#Scrap the page to check if it is available

def check_versusgamers(url):

	
	return False