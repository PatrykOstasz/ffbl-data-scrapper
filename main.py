import logging

from general.administrator import Administrator
from general.parameterslibrary import ParametersLibrary
from webdrivers.chromedriver import ChromeDriver

from scrappers.scrapperfactory import ScrapperFactory

def main():
    formatter = logging.Formatter('%(asctime)s %(levelname)s [ %(module)s ] %(funcName)s() : %(message)s')
    fileHandler = logging.FileHandler('sample.log')
    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(logging.INFO)

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(logging.INFO)

    logger = logging.getLogger('root')
    logger.setLevel(logging.INFO)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


    logging.info("Initializing configuration")

    miscParameters = ParametersLibrary.getParameters('misc')

    webDriverParameters = ParametersLibrary.getParameters('webdriver')
    chrome = ChromeDriver(webDriverParameters)

    scrappers = []
    for name in ScrapperFactory.SCRAPPER_NAMES:
        scrappers.append(ScrapperFactory.create(name, 
                                                chrome, 
                                                miscParameters, 
                                                ParametersLibrary.getParameters(name)))


    administrator = Administrator(chrome, scrappers)
    administrator.startScraping()
    administrator.saveToCSV('database.csv')
    administrator.saveToExcel('results.xlsx')

if __name__ == "__main__":
    main()


