import time

from bs4 import BeautifulSoup
from contextlib import closing
from selenium.webdriver import Edge
import pandas as pd

def convertFromWsToWebWs(name):
    return name.replace(" ", "%20")

search = "listing?string="
buynow = "offerTypeBuyNow=1"
logicaland = "&"
searchName = "Final Fantasy"

url = "https://allegro.pl/" + search + convertFromWsToWebWs(searchName) + logicaland + buynow

with closing(Edge()) as browser:
    browser.get(url)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

itemsWithPrices = []
for item in soup.find_all('article'):
    tempList = str(item.get('aria-label')).split(", ")
    if tempList != ['None']:
        itemsWithPrices.append(tempList)

data = pd.DataFrame(itemsWithPrices, columns=['name', 'price', 'x', 'y', 'z'])
print(data)