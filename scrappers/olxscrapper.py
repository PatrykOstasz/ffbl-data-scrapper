from selenium.webdriver.common.by import By

from scrappers.basescrapper import BaseScrapper

class OlxScrapper(BaseScrapper):
    def __init__(self, driver, misc, params) -> None:
        super().__init__(driver, misc, params)

    def acceptCookies(self):
        self._driver.find_element(By.XPATH, self._scrapperParams['xpath.cookies']).click()


    def findPageCount(self):
        pageList = self._driver.find_elements(By.XPATH, self._scrapperParams['xpath.pageCount'])
        pageCountL = []
        for page in pageList:
            pageCountL.append(page.get_attribute('aria-label'))
        pageCount =pageCountL[-1].split()
        return int(pageCount[1])


    def findProductNames(self):
        productNames = []
        for element in self._driver.find_elements(By.TAG_NAME, self._scrapperParams['xpath.productNames']):
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
        self._driver.find_element(By.XPATH, self._scrapperParams['xpath.pagination']).click()


    @staticmethod
    def processPrices(prices):
        processedPrices = []
        for item in prices:
            if 'do negocjacji' in item:
                processedPrices.append(item.replace('\ndo negocjacji', ''))
            else:
                processedPrices.append(item)
        return processedPrices
