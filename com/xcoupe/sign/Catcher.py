import requests
from bs4 import BeautifulSoup
import os

resp = requests.get('https://www.baidu.com')
rutf8 = resp.content.decode('utf-8')
soup = BeautifulSoup(rutf8,'html5lib')
print(soup.div['id'])