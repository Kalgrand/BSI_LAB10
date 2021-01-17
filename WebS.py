"""
Autor: Michał Degowski
"""

import pprint
import requests
import re
from bs4 import BeautifulSoup

search = input("Search:")
results = 10
response = requests.get(f"https://www.google.com/search?q={search}&num={results}")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all(attrs = {'class': 'ZINbbc'})
results = [re.search('\/url\?q\=(.*)\&sa',str(i.find('a')['href'])) for i in result]
links = [i.group(1) for i in results if i != None]
pprint.pprint(links)

