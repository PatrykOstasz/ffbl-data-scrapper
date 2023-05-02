import yaml

from selenium.webdriver import ChromeOptions
from yaml.loader import BaseLoader
from admin.webdriverparameters import WebDriverParameters

class ChromeDriverOptions:
    def __init__(self) -> None:
        self._options = ChromeOptions()
        p = WebDriverParameters()

        self._options.add_argument(p.headlessMode)
        self._options.add_argument(p.disableGpu)
        self._options.add_argument(p.disableAutomationControlledFlag)

        (exSwitchesKey, exSwitchesValues), = p.expSwitches.items()
        (exAutoExtensionKey, exAutoExtensionValue), = p.expAutomationExtension.items()
        self._options.add_experimental_option(exSwitchesKey, exSwitchesValues)
        self._options.add_experimental_option(exAutoExtensionKey, exAutoExtensionValue)

    @property
    def options(self):
        return self._options