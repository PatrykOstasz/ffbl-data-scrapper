import random

from selenium.webdriver import Edge
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from drivers.EdgeDriverOptions import EdgeDriverOptions

class EdgeDriver:
    def __init__(self, vendorFullUrl) -> None:
        self._vendorFullUrl = vendorFullUrl

        self._edgeDriverOptions = EdgeDriverOptions()
        self._automaticService = Service(EdgeChromiumDriverManager().install())
        self._driver = None


    def __del__(self):
        self._driver.quit()

    def execute(self):
        self._driver = Edge(service=self._automaticService, options=self._edgeDriverOptions.options)

        #Changing the property of the navigator value for webdriver to undefined
        self._driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self._driver.get(self._vendorFullUrl)
        _wait = WebDriverWait(self._driver, random.randint(10000, 20000))
        self._driver.execute_script("window.scrollBy(0,{pixels})".format(pixels=random.randint(100, 1000)),"")

    @property
    def driver(self):
        return self._driver
