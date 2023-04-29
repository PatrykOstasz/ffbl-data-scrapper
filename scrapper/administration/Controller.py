import pandas as pd

from vendors.OlxVendor import OlxVendor
from vendors.AmazonVendor import AmazonVendor
from vendors.AllegroLVendor import AllegroLVendor
from drivers.ChromeDriver import ChromeDriver


class Controller:
    def __init__(self) -> None:
        olx = OlxVendor()
        amazon = AmazonVendor()
        allegroL = AllegroLVendor()
        self._vendors = [allegroL]
        self._data = []
    
    def startScraping(self):
        for vendor in self._vendors:
            self._processData(vendor)

    def _processData(self, vendor):
        chromeDriver = ChromeDriver(vendor.fullUrl)
        chromeDriver.execute()
        vendorData = vendor.startScrapingData(chromeDriver.driver)
        vendor.processScrappedData(vendorData)
        self._data.extend(vendor.processedData)

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

