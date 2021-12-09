import requests
from bs4 import BeautifulSoup

response = requests.get('https://maquia.hpplus.jp/makeup/news/')
soup = BeautifulSoup(response.text,'lxml')
articles = soup.findAll('div', class_='article-card-media')

for article in articles:
   link = article.a.get('href')
   print(link)