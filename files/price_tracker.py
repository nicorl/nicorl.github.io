import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.es/ProCase-Inteligente-Transl%C3%BAcido-Esmerilado-Pulgadas/dp/B071J2SSYH/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=ipad+air+3+case&qid=1577997734&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMVJMMUFGSzE0VENUJmVuY3J5cHRlZElkPUEwODczOTk2MTg4MDdMVkFXODVSNCZlbmNyeXB0ZWRBZElkPUEwNzU3MjQxR1BNSkVMTDBMQTlMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html5lib')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	print(title.strip())
	print(price)


check_price()