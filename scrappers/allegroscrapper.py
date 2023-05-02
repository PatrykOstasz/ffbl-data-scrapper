import random
import time

from selenium.webdriver.common.by import By


class AllegroScrapper:
    def __init__(self) -> None:
        self._data = []
        self._fullUrl = 'https://allegro.pl/listing?string=final%20fantasy&offerTypeBuyNow=1'

    def startScrapingData(self, driver):
        time.sleep(random.randint(1, 5))

        products = []
        for element in driver.find_elements(By.TAG_NAME, 'article'):
            products.append(element.get_attribute('aria-label'))
        print(products)
        return products

    
    def processScrappedData(self, products):
        for item in products:
            processedItem = str(item).split(', ')
            if processedItem != ['None'] and len(processedItem) == 2:
                self._data.append(processedItem)
    

    @property
    def fullUrl(self):
        return self._fullUrl
    

    @property
    def processedData(self):
        return self._data