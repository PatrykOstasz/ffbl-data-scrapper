import yaml

from yaml.loader import Loader

PARAMETERS_FILENAME = "configuration/parameters.yaml"

class ParameterParser:
    _instance = None
    _parameters = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ParameterParser, cls).__new__(cls)
        return cls._instance


    def __init__(cls) -> None:
        cls._instance._parseParametersFile(PARAMETERS_FILENAME)


    @classmethod
    def _parseParametersFile(cls, filename):
        with open(filename, 'r') as file:
            cls._parameters = list(yaml.load_all(file, Loader=Loader))


    @classmethod
    def getWebDriverParams(cls):
        for param in cls._parameters:
            if param['section'] == 'webdriver':
                return param
        raise Exception('ERROR: param not defined')


    @classmethod
    def getAllegroLocalScrapperParams(cls):
        for param in cls._parameters:
            if param['section'] == 'scrapper.allegrolocal':
                return param
        raise Exception('ERROR: param not defined')


    @classmethod
    def getAmazonScrapperParams(cls):
        for param in cls._parameters:
            if param['section'] == 'scrapper.amazon':
                return param
        raise Exception('ERROR: param not defined')


    @classmethod
    def getOlxScrapperParams(cls):
        for param in cls._parameters:
            if param['section'] == 'scrapper.olx':
                return param
        raise Exception('ERROR: param not defined')


    @classmethod
    def getMiscParams(cls):
        for param in cls._parameters:
            if param['section'] == 'misc':
                return param
        raise Exception('ERROR: param not defined')
