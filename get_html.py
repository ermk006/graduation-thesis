import requests
from bs4 import BeautifulSoup

response = requests.get('https://maquia.hpplus.jp/makeup/')
soup = BeautifulSoup(response.text,'lxml')
title = soup.title.string
print(title)