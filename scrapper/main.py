import time

from bs4 import BeautifulSoup
from contextlib import closing
from selenium.webdriver import Edge

url = "https://allegro.pl"


with closing(Edge()) as browser:
    browser.get(url)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    print(soup.prettify())