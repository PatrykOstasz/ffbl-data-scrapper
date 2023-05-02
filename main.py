from general.administrator import Administrator
from general.parameters_library.miscparameters import MiscParameters
from general.parameters_library.scrapperparameters import *
from general.parameters_library.webdriverparameters import WebDriverParameters
from scrappers.allegrolocalscrapper import AllegroLocalScrapper
from scrappers.amazonscrapper import AmazonScrapper
from scrappers.olxscrapper import OlxScrapper
from webdrivers.chromedriver import ChromeDriver


def main():
    #getting parameters
    miscP = MiscParameters()

    allegroLocalP = AllegroLocalScrapperParameters()
    allegroLocalS = AllegroLocalScrapper(allegroLocalP, miscP)

    amazonP = AmazonScrapperParameters()
    amazonS = AmazonScrapper(amazonP, miscP)

    olxP = OlxScrapperParameters()
    olxS = OlxScrapper(olxP, miscP)
    
    scrappers = [allegroLocalS, amazonS, olxS]

    webDriverP = WebDriverParameters()
    chrome = ChromeDriver(webDriverP)

    administrator = Administrator(chrome, scrappers)
    administrator.startScraping()
    administrator.print()
    administrator.saveToFile('results.xlsx')

if __name__ == "__main__":
    main()


