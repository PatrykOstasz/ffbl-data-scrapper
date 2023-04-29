import yaml

from selenium.webdriver import EdgeOptions
from yaml.loader import BaseLoader

class EdgeDriverOptions:
    def __init__(self) -> None:
        self._options = EdgeOptions()
        parameters = self._readParameters_()

        self._options.use_chromium = parameters['useChromium']
        self._options.add_argument(parameters['disable.AutomationControlledFlag'])
        self._options.add_experimental_option(parameters['switches']["excludeSwitches"], parameters['switches']['value'])
        self._options.add_experimental_option(parameters["turnOffUserAutomationExtension"], parameters['value'])
        #self._options.add_argument(parameters['headlessMode'])
        #self._options.add_argument(parameters['disable.Gpu'])
        
    @staticmethod
    def _readParameters_():
        with open('config/EdgeParameters.yaml', 'r') as file:
            parameters = yaml.load(file, Loader=BaseLoader)
        return parameters

    @property
    def options(self):
        return self._options





