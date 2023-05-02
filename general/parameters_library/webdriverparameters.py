from general.parameters_library.parameterparser import ParameterParser

def validate(driver):
    keys = ['headlessMode',
            'disable.Gpu',
            'disable.AutomationControlledFlag',
            'script.navigator',
            'experimental.switches',
            'experimental.automaExtension']
    try:
        for k in keys:
            value = driver[k]
    except KeyError as err:
        print('Exception Caught! Value for specific key is not found!')
        raise


class WebDriverParameters:
    def __init__(self) -> None:
        self._webdriver = ParameterParser().getWebDriverParams()
        validate(self._webdriver)

    @property
    def headlessMode(self):
        return self._webdriver['headlessMode']
    
    @property
    def disableGpu(self):
        return self._webdriver['disable.Gpu']
    
    @property
    def disableAutomationControlledFlag(self):
        return self._webdriver['disable.AutomationControlledFlag']
    
    @property
    def scriptNavigator(self):
        return self._webdriver['script.navigator']
    
    @property
    def expSwitches(self):
        return self._webdriver['experimental.switches']
    
    @property
    def expAutomationExtension(self):
        return self._webdriver['experimental.automaExtension']