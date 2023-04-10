import random
import re
import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


import yaml

from selenium.webdriver import EdgeOptions
from yaml.loader import BaseLoader

from edgeoptions import EdgeDriverOptions
from vendor import AllegroVendor

class EdgeDriver:
    def __init__(self) -> None:
        self._automaticService = Service(EdgeChromiumDriverManager().install())

        edge = EdgeDriverOptions()

        self._driver = Edge(service=self._automaticService, options=edge.edgeOptions)
        self._scrappedData = []

        #Changing the property of the navigator value for webdriver to undefined
        self._driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def __del__(self):
        self._driver.quit()

    def startScrapping(self):
        allegro = AllegroVendor()
        self._driver.get(allegro.fullUrl)
        _wait = WebDriverWait(self._driver, random.randint(3, 7))
        self._driver.execute_script("window.scrollBy(0,{pixels})".format(pixels=random.randint(100, 1000)),"")
    
    def getScrappedData(self):
        time.sleep(random.randint(2, 6))
        for element in self._driver.find_elements(By.TAG_NAME, 'article'):
            tempList = re.split(', \d+' , str(element.get_attribute('aria-label')))
            if tempList != ['None']:
                self._scrappedData.append(tempList)
    
    def printData(self):
        pass