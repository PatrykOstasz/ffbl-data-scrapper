import logging
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

    def startScraping(self):
        logging.info('data scrapping initialized')
        for scrapper in self._scrappers:
            self.processData(scrapper)


    def processData(self, scrapper):
        logging.info('process gathered data')
        self._webdriver.execute(scrapper.fullUrl)
        scrappedData = scrapper.startScrapingData()
        scrapper.processScrappedData(scrappedData)
        self._data.extend(scrapper.processedData)


    def saveToExcel(self, filename):
        logging.info(f'saving data to excel worksheet: {filename}')

        if len(self._data) != 0:
            data = pd.DataFrame(self._data, columns=['name', 'price', 'code', 'url'])
            data.to_excel(filename, index=False)
        else:
             logging.error('Data cannot be saved when empty')


    def saveToCSV(self, filename):
        logging.info(f'saving data to csv: {filename}')
        
        if len(self._data) != 0:
            data = pd.DataFrame(self._data, columns=['name', 'price', 'code', 'url'])
            data.to_csv(filename, sep=';', index=False)
        else:
           logging.error('Data cannot be saved when empty') 
