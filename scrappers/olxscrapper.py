import random
import time

from selenium.webdriver.common.by import By


class OlxScrapper:
    def __init__(self, olxParams, miscParams) -> None:
        self._olxParams = olxParams
        self._miscParams = miscParams     
        self._data = []
        self._fullUrl = self._olxParams.fullUrl
        self._driver = None


    def startScrapingData(self):
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
        for item in prices:
            if 'do negocjacji' in item:
                processedPrices.append(item.replace('\ndo negocjacji', ''))
            else:
                processedPrices.append(item)
        
        self._data = [list(elem) for elem in zip(names, processedPrices)]


    def setWebDriver(self, driver):
        self._driver = driver.driver


    def _acceptCookies(self):
        self._driver.find_element(By.XPATH, self._olxParams.cookies).click()


    def _findPageCount(self):
        _pageList = self._driver.find_elements(By.XPATH, self._olxParams.pageCount)
        _pageCountL = []
        for page in _pageList:
            _pageCountL.append(page.get_attribute('aria-label'))
        print(_pageCountL)
        _pageCount =_pageCountL[-1].split()
        print(_pageCount[1])
        return int(_pageCount[1])


    def _findProductNames(self):
        _productNames = []
        for element in self._driver.find_elements(By.TAG_NAME, self._olxParams.productNames):
            _productNames.append(str(element.text))
        return _productNames


    def _findProductPrices(self):
        _productPrices = []
        for element in self._driver.find_elements(By.XPATH, self._olxParams.productPrices):
            _productPrices.append(element.text)
        return _productPrices


    def _turnPage(self):
        self._driver.find_element(By.XPATH, self._olxParams.pagination).click()
        time.sleep(random.randint(self._miscParams.waitTimeMin, self._miscParams.waitTimeMax))  


    @property
    def fullUrl(self):
        return self._fullUrl


    @property
    def processedData(self):
        return self._data
