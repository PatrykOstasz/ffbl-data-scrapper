import random
import time

from selenium.webdriver.common.by import By


class OlxScrapper:
    def __init__(self) -> None:       
        self._data = []
        self._fullUrl = "https://www.olx.pl/oferty/q-final-fantasy/"


    def startScrapingData(self, driver):
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
        for item in prices:
            if 'do negocjacji' in item:
                processedPrices.append(item.replace('\ndo negocjacji', ''))
            else:
                processedPrices.append(item)
        
        self._data = [list(elem) for elem in zip(names, processedPrices)]


    @staticmethod
    def _acceptCookies(driver):
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()


    @staticmethod
    def _findPageCount(driver):
        _pageList = driver.find_elements(By.XPATH, "//li[@data-testid='pagination-list-item']")
        _pageCountL = []
        for page in _pageList:
            _pageCountL.append(page.get_attribute('aria-label'))
        print(_pageCountL)
        _pageCount =_pageCountL[-1].split()
        print(_pageCount[1])
        return int(_pageCount[1])


    @staticmethod
    def _findProductNames(driver):
        _productNames = []
        for element in driver.find_elements(By.TAG_NAME, 'h6'):
            _productNames.append(str(element.text))
        return _productNames


    @staticmethod
    def _findProductPrices(driver):
        _productPrices = []
        for element in driver.find_elements(By.XPATH, "//p[@data-testid='ad-price']"):
            _productPrices.append(element.text)
        return _productPrices


    @staticmethod
    def _turnPage(driver):
        driver.find_element(By.XPATH, "//a[@data-testid='pagination-forward']").click()
        time.sleep(random.randint(1, 5))  


    @property
    def fullUrl(self):
        return self._fullUrl


    @property
    def processedData(self):
        return self._data
