---
title: "Amazon Price Tracker"
excerpt: "Python code for price tracking at amazon"
collection: portfolio
---

A small python code can allow us to track any single tag in a web. It's usefull for amazon, also for others kind of shops that haven't a tracker yet.

# Instructions for using

First, type on the terminal:

> chcp 65001

That's for character encoding. [More info here](https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window)

Then, install bs4 and html5lib:

> conda install bs4

> conda install html5lib

Second step: google "my user agent" and add the line in the header asignation below.

<img src='/images/my-user-agent-google.png'>

Third, add this in an empty python file and save as `price_tracker.py`

```python
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.es/ProCase-Inteligente-Transl%C3%BAcido-Esmerilado-Pulgadas/dp/B071J2SSYH/ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=ipad+air+3+case&qid=1577997734&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMVJMMUFGSzE0VENUJmVuY3J5cHRlZElkPUEwODczOTk2MTg4MDdMVkFXODVSNCZlbmNyeXB0ZWRBZElkPUEwNzU3MjQxR1BNSkVMTDBMQTlMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html5lib')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	print(title.strip())
	print(price)


check_price()
```

> python price_tracker.py

```terminal
ProCase Funda 10,5” iPad Pro 2017/iPad Air 2019, Estuche Inteligente Ultra Delgada Ligera con Soporte Reverso Translúcido Esmerilado para iPad Air 3.ª Generación/iPad Pro 10.5 Pulgadas -Azul Marino
13,99 €
```

## Details

To know what is the id you are looking for, you shoud go to the website, open the inspector and query about the tag.

<img src='/images/priceBlock2.png'>
<img src='/images/productTitle2.png'>
