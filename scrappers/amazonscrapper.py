import random
import re
import time

from selenium.webdriver.common.by import By


class AmazonScrapper:
    def __init__(self, amazonParams, miscParams) -> None:    
        self._data = []
        self._fullUrl = "https://www.amazon.pl/s?k=final+fantasy&crid=2PXQDRZOTKAN6&sprefix=%2Caps%2C118&ref=nb_sb_ss_recent_1_0_recent"
        self._driver = None


    def startScrapingData(self):
        #cookies form will start each time on a 'clean' browser
        self._acceptCookies()
        time.sleep(random.randint(1, 5))

        _pageCount = self._findPageCount()

        _productNames = self._findProductNames()
        _productPrices = self._findProductPrices()
        
        for page in range(1, _pageCount):
            self._turnPage()
            _productNames.extend(self._findProductNames())
            _productPrices.extend(self._findProductPrices())

        return _productNames, _productPrices


    def processScrappedData(self, products):
        names, prices = products
        processedPrices = []
        for price in prices:
            if '\n' in price:
                processedPrices.append(price.replace('\n', ','))
            else:
                processedPrices.append(price)
        self._data = [list(elem) for elem in zip(names, processedPrices)]


    def setWebDriver(self, driver):
        self._driver = driver.driver


    def _acceptCookies(self):
        self._driver.find_element(By.XPATH, "//input[@id='sp-cc-accept']").click()


    def _findPageCount(self):
        return int(self._driver.find_element(By.XPATH, "//span[@class='s-pagination-item s-pagination-disabled']").text)


    def _findProductNames(self):
        _productNames = []
        for element in self._driver.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']"):
            _productNames.append(str(element.text))
        return _productNames


    def _findProductPrices(self):
        _productPrices = []
        for element in self._driver.find_elements(By.XPATH, "//span[@class='a-price']"):
            _productPrices.append(element.text)
        return _productPrices


    def _turnPage(self):
        self._driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']").click()
        time.sleep(random.randint(1, 5))


    @property
    def fullUrl(self):
        return self._fullUrl

   
    @property
    def processedData(self):
        return self._data