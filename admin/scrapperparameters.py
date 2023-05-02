from admin.parameterparser import ParameterParser

def validate(scrapper):
    keys = ['fullUrl',
            'xpath.cookies',
            'xpath.pageCount',
            'xpath.productNames',
            'xpath.productPrices',
            'xpath.pagination']
    try:
        for k in keys:
            temp = scrapper[k]
    except KeyError as err:
        print('Exception Caught! Value for specific key is not found!')
        raise

class AllegroLocalScrapperParameters:
    def __init__(self) -> None:
        self._allegroLocal = ParameterParser().getAllegroLocalScrapperParams()
        validate(self._allegroLocal)
    
    @property
    def fullUrl(self):
        return self._allegroLocal['fullUrl']

    @property
    def cookies(self):
        return self._allegroLocal['xpath.cookies']
    
    @property
    def pageCount(self):
        return self._allegroLocal['xpath.pageCount']
    
    @property
    def productNames(self):
        return self._allegroLocal['xpath.productNames']
    
    @property
    def productPrices(self):
        return self._allegroLocal['xpath.productPrices']
    
    @property
    def pagination(self):
        return self._allegroLocal['xpath.pagination']


class AmazonScrapperParameters:
    def __init__(self) -> None:
        self._amazon = ParameterParser().getAmazonScrapperParams()
        validate(self._amazon)
    
    @property
    def fullUrl(self):
        return self._amazon['fullUrl']

    @property
    def cookies(self):
        return self._amazon['xpath.cookies']
    
    @property
    def pageCount(self):
        return self._amazon['xpath.pageCount']
    
    @property
    def productNames(self):
        return self._amazon['xpath.productNames']
    
    @property
    def productPrices(self):
        return self._amazon['xpath.productPrices']
    
    @property
    def pagination(self):
        return self._amazon['xpath.pagination']


class OlxScrapperParameters:
    def __init__(self) -> None:
        self._olx = ParameterParser().getOlxScrapperParams()
        validate(self._olx)

    @property
    def fullUrl(self):
        return self._olx['fullUrl']

    @property
    def cookies(self):
        return self._olx['xpath.cookies']
    
    @property
    def pageCount(self):
        return self._olx['xpath.pageCount']
    
    @property
    def productNames(self):
        return self._olx['xpath.productNames']
    
    @property
    def productPrices(self):
        return self._olx['xpath.productPrices']
    
    @property
    def pagination(self):
        return self._olx['xpath.pagination']
