import random
import time

from selenium.webdriver.common.by import By


class AllegroLocalScrapper:
    def __init__(self) -> None:       
        self._data = []
        self._fullUrl = "https://allegrolokalnie.pl/oferty/q/final%20fantasy?typ=kup-teraz"
    

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
        
        #creating whole prices with nominal
        processedPrices = []
        for elem in prices:
            tempPrice = elem + ",00zł"
            processedPrices.append(tempPrice)
        
        self._data = [list(elem) for elem in zip(names, processedPrices)]
    

    @staticmethod
    def _acceptCookies(driver):
        driver.find_element(By.XPATH, "//button[@id='cookies_confirm']").click()


    @staticmethod
    def _findPageCount(driver):
        _paginationItem = []
        for elem in driver.find_elements(By.XPATH, "//span[@class='ml-text-medium ml-text-color-secondary ml-pagination__count']"):
                _paginationItem.append(str(elem.text))
        return int(_paginationItem[-1].split()[-1])


    @staticmethod
    def _findProductNames(driver):
        _productNames = []
        for element in driver.find_elements(By.XPATH, "//h3[@class='mlc-itembox__title']"):
            _productNames.append(str(element.text))
        return _productNames


    @staticmethod
    def _findProductPrices(driver):
        _productPrices = []
        for element in driver.find_elements(By.XPATH, "//span[@class='ml-offer-price__dollars']"):
            _productPrices.append(element.text)
        return _productPrices


    @staticmethod
    def _turnPage(driver):
        element = driver.find_element(By.XPATH, "//a[@class='ml-pagination__link']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(random.randint(1, 5))  


    @property
    def fullUrl(self):
        return self._fullUrl
    

    @property
    def processedData(self):
        return self._data