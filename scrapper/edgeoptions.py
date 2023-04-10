import yaml

from selenium.webdriver import EdgeOptions
from yaml.loader import BaseLoader


class EdgeDriverOptions:
    def __init__(self) -> None:
        self._edgeOptions = EdgeOptions()
        options = self.parseData()

        self._edgeOptions.use_chromium = options['useChromium']
        self._edgeOptions.add_argument(options['disable.AutomationControlledFlag'])
        self._edgeOptions.add_experimental_option(options['switches']["excludeSwitches"], options['switches']['value'])
        self._edgeOptions.add_experimental_option(options["turnOffUserAutomationExtension"], options['value'])

    def parseData(self):
        with open('config/edge-options.yaml', 'r') as file:
            options = yaml.load(file, Loader=BaseLoader)
        return options

    @property
    def edgeOptions(self):
        return self._edgeOptions





