import yaml

from yaml.loader import Loader

PARAMETERS_FILENAME = "configuration/parameters.yaml"

class ParameterParser:
    instance = None
    parameters = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(ParameterParser, cls).__new__(cls)
        return cls.instance


    def __init__(cls) -> None:
        cls.instance.parseParametersFile(PARAMETERS_FILENAME)


    @classmethod
    def parseParametersFile(cls, filename):
        with open(filename, 'r') as file:
            cls.parameters = list(yaml.load_all(file, Loader=Loader))



class ParametersLibrary:
    def __init__(cls) -> None:
        pass

    @classmethod
    def getParameters(cls, category):
        for parameters in ParameterParser().parameters:
            if parameters['section'] == category:
                return parameters
        raise Exception('ERROR: parameter category not defined')

