import random
import re
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from drivers.ChromeDriverOptions import ChromeDriverOptions

class ChromeDriver:
    def __init__(self, vendorFullUrl) -> None:
        self._vendorFullUrl = vendorFullUrl

        self._chromeDriverOptions = ChromeDriverOptions()
        self._automaticService = Service(ChromeDriverManager().install())
        self._driver = None
        self._driver = Chrome(service=self._automaticService, options=self._chromeDriverOptions.options)

        #Changing the property of the navigator value for webdriver to undefined
        self._driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def __del__(self):
        self._driver.quit()

    def execute(self):
        self._driver.get(self._vendorFullUrl)
        _wait = WebDriverWait(self._driver, random.randint(3, 7))
        #self._driver.execute_script("window.scrollBy(0,{pixels})".format(pixels=random.randint(100, 1000)),"")

    @property
    def driver(self):
        return self._driver