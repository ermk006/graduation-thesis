import requests
from bs4 import BeautifulSoup

for page in range(1,11):
   r = requests.get("https://maquia.hpplus.jp/makeup/news/?page="+str(page))
   r.encoding = r.apparent_encoding
   response = r.text

soup = BeautifulSoup(response,'lxml')
articles = soup.findAll('div', class_='article-card-media')

for article in articles:
   link = article.a.get('href')
   print(link)