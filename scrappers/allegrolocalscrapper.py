from selenium.webdriver.common.by import By

from scrappers.basescrapper import BaseScrapper

class AllegroLocalScrapper(BaseScrapper):
    def __init__(self, driver, misc, params) -> None:
        super().__init__(driver, misc, params)
        self.scrapperCode = 'AL'

    def acceptCookies(self):
        self._driver.find_element(By.XPATH, self._scrapperParams['xpath.cookies']).click()


    def findPageCount(self):
        paginationItem = []
        for elem in self._driver.find_elements(By.XPATH, self._scrapperParams['xpath.pageCount']):
                paginationItem.append(str(elem.text))
        return int(paginationItem[-1].split()[-1])


    def findProductNames(self):
        productNames = []
        for element in self._driver.find_elements(By.XPATH, self._scrapperParams['xpath.productNames']):
            productNames.append(str(element.text))
        return productNames


    def findProductPrices(self):
        productPrices = []
        for element in self._driver.find_elements(By.XPATH, self._scrapperParams['xpath.productPrices']):
            productPrices.append(element.text)
        return productPrices

    def findProductUrls(self):
        productUrls = []
        for element in self._driver.find_elements(By.XPATH, self._scrapperParams['xpath.productUrls']):
            productUrls.append(element.get_attribute('href'))

        return productUrls


    def turnPage(self):
        element = self._driver.find_element(By.XPATH, self._scrapperParams['xpath.pagination'])
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        self._driver.execute_script("arguments[0].click();", element)

    @staticmethod
    def processPrices(prices):   
        processedPrices = []
        for elem in prices:
            tempPrice = elem + ",00zł"
            processedPrices.append(tempPrice)
        return processedPrices


