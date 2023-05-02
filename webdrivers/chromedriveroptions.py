import yaml

from selenium.webdriver import ChromeOptions
from yaml.loader import BaseLoader

class ChromeDriverOptions:
    def __init__(self, params) -> None:
        self._options = ChromeOptions()

        self._options.add_argument(params.headlessMode)
        self._options.add_argument(params.disableGpu)
        self._options.add_argument(params.disableAutomationControlledFlag)

        (exSwitchesKey, exSwitchesValues), = params.expSwitches.items()
        (exAutoExtensionKey, exAutoExtensionValue), = params.expAutomationExtension.items()
        self._options.add_experimental_option(exSwitchesKey, exSwitchesValues)
        self._options.add_experimental_option(exAutoExtensionKey, exAutoExtensionValue)

    @property
    def options(self):
        return self._options