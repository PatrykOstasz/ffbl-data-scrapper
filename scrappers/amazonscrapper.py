import random
import re
import time

from selenium.webdriver.common.by import By


class AmazonScrapper:
    def __init__(self) -> None:    
        self._data = []
        self._fullUrl = "https://www.amazon.pl/s?k=final+fantasy&crid=2PXQDRZOTKAN6&sprefix=%2Caps%2C118&ref=nb_sb_ss_recent_1_0_recent"


    def startScrapingData(self, driver):
        #cookies form will start each time on a 'clean' browser
        self._acceptCookies(driver)
        time.sleep(random.randint(1, 5))

        _pageCount = self._findPageCount(driver)

        _productNames = self._findProductNames(driver)
        _productPrices = self._findProductPrices(driver)
        
        for page in range(1, _pageCount):
            self._turnPage(driver)
            _productNames.extend(self._findProductNames(driver))
            _productPrices.extend(self._findProductPrices(driver))

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


    @staticmethod
    def _acceptCookies(driver):
        driver.find_element(By.XPATH, "//input[@id='sp-cc-accept']").click()


    @staticmethod
    def _findPageCount(driver):
        return int(driver.find_element(By.XPATH, "//span[@class='s-pagination-item s-pagination-disabled']").text)


    @staticmethod
    def _findProductNames(driver):
        _productNames = []
        for element in driver.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']"):
            _productNames.append(str(element.text))
        return _productNames


    @staticmethod
    def _findProductPrices(driver):
        _productPrices = []
        for element in driver.find_elements(By.XPATH, "//span[@class='a-price']"):
            _productPrices.append(element.text)
        return _productPrices


    @staticmethod
    def _turnPage(driver):
        driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']").click()
        time.sleep(random.randint(1, 5))


    @property
    def fullUrl(self):
        return self._fullUrl

   
    @property
    def processedData(self):
        return self._data