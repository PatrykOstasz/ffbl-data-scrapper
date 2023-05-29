import random

from webdrivers.chromedriveroptions import ChromeDriverOptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
    def __init__(self, params) -> None:
        self._chromeDriverOptions = ChromeDriverOptions(params)
        self._automaticService = Service(ChromeDriverManager().install())
        self._driver = Chrome(service=self._automaticService, options=self._chromeDriverOptions.options)

        #Changing the property of the navigator value for webdriver to undefined
        self._driver.execute_script(params['script.navigator'])


    def __del__(self):
        self._driver.quit()


    def execute(self, url):
        self._driver.get(url)
        _wait = WebDriverWait(self._driver, random.randint(1, 5))


    @property
    def driver(self):
        return self._driver