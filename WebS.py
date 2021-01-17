"""
Autor: Michał Degowski
"""

import threading
import pprint
import requests
import re
from bs4 import BeautifulSoup

print("Search: ")

def WebSearch():
    search = input()
    results = 10
    response = requests.get(f"https://www.google.com/search?q={search}&num={results}")
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all(attrs={'class': 'ZINbbc'})
    results = [re.search('\/url\?q\=(.*)\&sa', str(i.find('a')['href'])) for i in result]
    links = [i.group(1) for i in results if i != None]
    pprint.pprint(links)


watek = threading.Thread(target=WebSearch)
watek.start()
watek2 = threading.Thread(target=WebSearch)
watek2.start()
watek.join()
watek2.join()
