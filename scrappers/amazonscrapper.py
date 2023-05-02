import random
import re
import time

from selenium.webdriver.common.by import By


class AmazonScrapper:
    def __init__(self, amazonParams, miscParams) -> None:
        self._amazonParams = amazonParams
        self._miscParams = miscParams
        self._data = []
        self._fullUrl = self._amazonParams.fullUrl
        self._driver = None


    def startScrapingData(self):
        #cookies form will start each time on a 'clean' browser
        self._acceptCookies()
        time.sleep(random.randint(self._miscParams.waitTimeMin, self._miscParams.waitTimeMax))

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
        self._driver.find_element(By.XPATH, self._amazonParams.cookies).click()


    def _findPageCount(self):
        return int(self._driver.find_element(By.XPATH, self._amazonParams.pageCount).text)


    def _findProductNames(self):
        _productNames = []
        for element in self._driver.find_elements(By.XPATH, self._amazonParams.productNames):
            _productNames.append(str(element.text))
        return _productNames


    def _findProductPrices(self):
        _productPrices = []
        for element in self._driver.find_elements(By.XPATH, self._amazonParams.productPrices):
            _productPrices.append(element.text)
        return _productPrices


    def _turnPage(self):
        self._driver.find_element(By.XPATH, self._amazonParams.pagination).click()
        time.sleep(random.randint(self._miscParams.waitTimeMin, self._miscParams.waitTimeMax))


    @property
    def fullUrl(self):
        return self._fullUrl

   
    @property
    def processedData(self):
        return self._data