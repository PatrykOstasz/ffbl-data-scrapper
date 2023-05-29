from selenium.webdriver.common.by import By

from scrappers.basescrapper import BaseScrapper

class AmazonScrapper(BaseScrapper):
    def __init__(self, driver, misc, params) -> None:
        super().__init__(driver, misc, params)

    def acceptCookies(self):
        self._driver.find_element(By.XPATH, self._scrapperParams['xpath.cookies']).click()


    def findPageCount(self):
        return int(self._driver.find_element(By.XPATH, self._scrapperParams['xpath.pageCount']).text)


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


    def turnPage(self):
        self._driver.find_element(By.XPATH, self._scrapperParams['xpath.pagination']).click()

    @staticmethod
    def processPrices(prices):
        processedPrices = []
        for price in prices:
            if '\n' in price:
                processedPrices.append(price.replace('\n', ','))
            else:
                processedPrices.append(price)
        return processedPrices
