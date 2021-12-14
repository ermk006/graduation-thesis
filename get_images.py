import requests
import re
import uuid
from bs4 import BeautifulSoup
import time

url = "https://maquia.hpplus.jp/makeup/news/65455/"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
imgs = soup.find_all('img',src=re.compile('^https://img-maquia.hpplus.jp/common/large/image/'))
for img in imgs:
        print(img['src'])
        r = requests.get(img['src'])
        time.sleep(1)
        with open(str('./picture/')+str(uuid.uuid4())+str('.jpeg'),'wb') as file:
                file.write(r.content)