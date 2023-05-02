import random
import time

from selenium.webdriver.common.by import By

class AllegroLocalScrapper:
    def __init__(self, allegroParams, miscParams) -> None:     
        self._data = []
        self._fullUrl = "https://allegrolokalnie.pl/oferty/q/final%20fantasy?typ=kup-teraz"
        self._driver = None
    
    def setWebDriver(self, driver):
        self._driver = driver.driver

    def startScrapingData(self):
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
        
        #creating whole prices with nominal
        processedPrices = []
        for elem in prices:
            tempPrice = elem + ",00zł"
            processedPrices.append(tempPrice)
        
        self._data = [list(elem) for elem in zip(names, processedPrices)]
    

    def _acceptCookies(self):
        self._driver.find_element(By.XPATH, "//button[@id='cookies_confirm']").click()


    def _findPageCount(self):
        _paginationItem = []
        for elem in self._driver.find_elements(By.XPATH, "//span[@class='ml-text-medium ml-text-color-secondary ml-pagination__count']"):
                _paginationItem.append(str(elem.text))
        return int(_paginationItem[-1].split()[-1])


    def _findProductNames(self):
        _productNames = []
        for element in self._driver.find_elements(By.XPATH, "//h3[@class='mlc-itembox__title']"):
            _productNames.append(str(element.text))
        return _productNames


    def _findProductPrices(self):
        _productPrices = []
        for element in self._driver.find_elements(By.XPATH, "//span[@class='ml-offer-price__dollars']"):
            _productPrices.append(element.text)
        return _productPrices


    def _turnPage(self):
        element = self._driver.find_element(By.XPATH, "//a[@class='ml-pagination__link']")
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        self._driver.execute_script("arguments[0].click();", element)
        time.sleep(random.randint(1, 5))  


    @property
    def fullUrl(self):
        return self._fullUrl
    

    @property
    def processedData(self):
        return self._data