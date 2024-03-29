import logging
import random
import time

from abc import ABC, abstractmethod

class BaseScrapper(ABC):
    def __init__(self, driver, misc, params) -> None:
        self._miscParams = misc
        self._scrapperParams = params
        self._driver = driver.driver

        self._data = []
        self._code = self._scrapperParams['scrapperCode']

    def startScrapingData(self):
        logging.info(f"{self._scrapperParams['section']}: starting scrapping data")
        time.sleep(random.randint(self._miscParams['driver.waittime.min'], self._miscParams['driver.waittime.max']))

        self.acceptCookies()
        logging.info(f"{self._scrapperParams['section']}: accepting Cookies")

        time.sleep(random.randint(self._miscParams['driver.waittime.min'], self._miscParams['driver.waittime.max']))
        
        pageCount = self.findPageCount()
        logging.info(f"{self._scrapperParams['section']}: number of pages found: {pageCount}")

        productNames = self.findProductNames()
        productPrices = self.findProductPrices()
        productUrls = self.findProductUrls()

        logging.info(f"{self._scrapperParams['section']}: found product names: {len(productNames)}, found product prices: {len(productPrices)}")

        for page in range(1, pageCount):
            self.turnPage()
            logging.info(f"{self._scrapperParams['section']}: turning to page {page+1}")

            time.sleep(random.randint(self._miscParams['driver.waittime.min'], self._miscParams['driver.waittime.max']))

            productNames.extend(self.findProductNames())
            productPrices.extend(self.findProductPrices())
            productUrls.extend(self.findProductUrls())

            logging.info(f"{self._scrapperParams['section']}: found product names: {len(productNames)}, found product prices: {len(productPrices)}")
        
        return productNames, productPrices, productUrls
    
    def processScrappedData(self, products):
        logging.info(f"{self._scrapperParams['section']}: start preprocessing scrapped data")
        names, prices, urls = products
        codes = [self._code for code in range(len(names))]
        processedPrices = self.processPrices(prices)
        self._data = [list(elem) for elem in zip(names, processedPrices, codes, urls)]
    
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
    def findProductUrls(self):
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
        return self._scrapperParams['fullUrl']
