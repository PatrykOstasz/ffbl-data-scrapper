import yaml

from yaml.loader import BaseLoader

class AllegroVendor:
    def __init__(self) -> None:
        parameters = self.__parseData__()

        self._vendor = parameters['vendor']
        self._searchPrompt = parameters['searchPrompt']
        self._operatorAnd = parameters['operator.and']
        self._optionBuyNow = parameters['option.buyNow']
        self._searchName = parameters['searchName']

        self._fullUrl = self._vendor + self._searchPrompt + self._searchName + self._operatorAnd + self._optionBuyNow
    
    def __parseData__(self):
        with open('config/allegro.yaml') as file:
            parameters = yaml.load(file, Loader=BaseLoader)
        return parameters
    
    @property
    def fullUrl(self):
        return self._fullUrl