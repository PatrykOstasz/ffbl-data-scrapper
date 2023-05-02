import pandas as pd

from webdrivers.chromedriver import ChromeDriver
from scrappers.allegrolocalscrapper import AllegroLocalScrapper
from scrappers.amazonscrapper import AmazonScrapper
from scrappers.olxscrapper import OlxScrapper



class Administrator:
    def __init__(self, webdriver, scrappers) -> None:
        self._webdriver = webdriver
        self._scrappers = scrappers
        self._data = []

        for scrapper in self._scrappers:
            scrapper.setWebDriver(self._webdriver)

    def startScraping(self):
        for scrapper in self._scrappers:
            self._processData(scrapper)


    def _processData(self, scrapper):
        self._webdriver.execute(scrapper.fullUrl)
        scrappedData = scrapper.startScrapingData()
        scrapper.processScrappedData(scrappedData)
        self._data.extend(scrapper.processedData)


    def saveToFile(self, filename):
        if len(self._data) != 0:
            data = pd.DataFrame(self._data, columns=['name', 'price'])
            data.to_excel(filename, index=False)
        else:
            print('ERROR: Data cannot be saved when empty')


    def print(self):
        if len(self._data) != 0:
            data = pd.DataFrame(self._data, columns=['name', 'price'])
            print(data)
        else:
           print('ERROR: Data cannot be printed when empty') 
