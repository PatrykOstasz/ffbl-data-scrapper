import random
import time

from abc import ABC, abstractmethod

class BaseScrapper(ABC):
    def __init__(self, driver, misc, params) -> None:
        self._miscParams = misc
        self._scrapperParams = params
        self._driver = driver.driver

        self._data = []

    def startScrapingData(self):
        self.acceptCookies()
        time.sleep(random.randint(self._miscParams['driver.waittime.min'], self._miscParams['driver.waittime.max']))
        
        pageCount = self.findPageCount()

        productNames = self.findProductNames()
        productPrices = self.findProductPrices()

        for page in range(1, pageCount):
            self.turnPage()
            time.sleep(random.randint(self._miscParams['driver.waittime.min'], self._miscParams['driver.waittime.max']))

            productNames.extend(self.findProductNames())
            productPrices.extend(self.findProductPrices())
        
        return productNames, productPrices
    
    def processScrappedData(self, products):
        names, prices = products
        processedPrices = self.processPrices(prices)
        self._data = [list(elem) for elem in zip(names, processedPrices)]
    
    @abstractmethod
    def acceptCookies(self):
        pass

    @abstractmethod
    def findPageCount(self):
        pass

    @abstractmethod
    def findProductNames(self):
        pass

    @abstractmethod
    def findProductPrices(self):
        pass

    @abstractmethod
    def turnPage(self):
        pass
    
    @staticmethod
    @abstractmethod
    def processPrices(prices):
        pass

    @property
    def processedData(self):
        return self._data
    
    @property
    def fullUrl(self):
        print(self._scrapperParams['fullUrl'])
        return self._scrapperParams['fullUrl']