from general.administrator import Administrator
from general.parameterslibrary import ParametersLibrary
from webdrivers.chromedriver import ChromeDriver

from scrappers.scrapperfactory import ScrapperFactory

def main():
    #getting parameters
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
    administrator.print()
    administrator.saveToFile('results.xlsx')

if __name__ == "__main__":
    main()


