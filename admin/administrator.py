import pandas as pd

from drivers.chromedriver import ChromeDriver
from scrappers.allegrolocalscrapper import AllegroLocalScrapper
from scrappers.amazonscrapper import AmazonScrapper
from scrappers.olxscrapper import OlxScrapper


class Administrator:
    def __init__(self) -> None:
        olx = OlxScrapper()
        amazon = AmazonScrapper()
        allegroLocal = AllegroLocalScrapper()
        self._scrappers = [allegroLocal]
        self._data = []
    

    def startScraping(self):
        for scrapper in self._scrappers:
            self._processData(scrapper)


    def _processData(self, scrapper):
        chromeDriver = ChromeDriver(scrapper.fullUrl)
        chromeDriver.execute()
        vendorData = scrapper.startScrapingData(chromeDriver.driver)
        scrapper.processScrappedData(vendorData)
        self._data.extend(scrapper.processedData)


    def saveToFile(self):
        if len(self._data) != 0:
            data = pd.DataFrame(self._data, columns=['name', 'price'])
            data.to_excel('results.xlsx', index=False)
        else:
            print('ERROR: Data cannot be saved when empty')


    def print(self):
        if len(self._data) != 0:
            data = pd.DataFrame(self._data, columns=['name', 'price'])
            print(data)
        else:
           print('ERROR: Data cannot be printed when empty') 

