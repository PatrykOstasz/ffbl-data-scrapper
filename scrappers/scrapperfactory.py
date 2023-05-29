from scrappers.allegrolocalscrapper import AllegroLocalScrapper
from scrappers.amazonscrapper import AmazonScrapper
from scrappers.olxscrapper import OlxScrapper


class ScrapperFactory:

    SCRAPPER_NAMES = ['scrapper.amazon', 'scrapper.allegrolocal', 'scrapper.olx']

    @classmethod
    def create(cls, scrapperName, driver, misc, params):
        match scrapperName:
            case 'scrapper.amazon':
                return AmazonScrapper(driver, misc, params)
            case 'scrapper.allegrolocal':
                return AllegroLocalScrapper(driver, misc, params)
            case 'scrapper.olx':
                return OlxScrapper(driver, misc, params)