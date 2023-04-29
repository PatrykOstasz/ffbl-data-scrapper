import yaml

from selenium.webdriver import ChromeOptions
from yaml.loader import BaseLoader


class ChromeDriverOptions:
    def __init__(self) -> None:
        self._options = ChromeOptions()
        parameters = self._readParameters()

        self._options.add_argument(parameters['headlessMode'])
        self._options.add_argument(parameters['disable.Gpu'])
        self._options.add_argument(parameters['disable.AutomationControlledFlag'])
        self._options.add_experimental_option(parameters['switches']["excludeSwitches"], parameters['switches']['value'])
        self._options.add_experimental_option(parameters["turnOffUserAutomationExtension"], parameters['value'])

    def _readParameters(self):
        with open('config/ChromeParameters.yaml', 'r') as file:
            parameters = yaml.load(file, Loader=BaseLoader)
        return parameters

    @property
    def options(self):
        return self._options