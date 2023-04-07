import time
import pandas as pd
import random

from selenium.webdriver import Edge
from selenium.webdriver import EdgeOptions
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

#this is for future testing
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

search = "listing?string="
buynow = "offerTypeBuyNow=1"
logicaland = "&"
searchName = "Final Fantasy"

url = "https://allegro.pl/" + search + searchName + logicaland + buynow

edge_options = EdgeOptions()
edge_options.use_chromium = True

#for now those have to be commented-out
#edge_options.add_argument('headless')
#edge_options.add_argument('disable-gpu')

# Adding argument to disable the AutomationControlled flag 
edge_options.add_argument('disable-blink-features=AutomationControlled')

# Exclude the collection of enable-automation switches 
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 

# Turn-off userAutomationExtension 
edge_options.add_experimental_option("useAutomationExtension", False) 

driver = Edge(service=Service('config/msedgedriver.exe'), options=edge_options)

# Changing the property of the navigator value for webdriver to undefined
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
time.sleep(random.randint(1, 5))

driver.get(url)

wait = WebDriverWait(driver, random.randint(1, 5)) 

itemsWithPrices = []
for element in driver.find_elements(By.TAG_NAME, 'article'):
    tempList = str(element.get_attribute('aria-label')).split(", ")
    if tempList != ['None']:
        itemsWithPrices.append(tempList)

data = pd.DataFrame(itemsWithPrices, columns=['name', 'price', 'x', 'y', 'z'])
print(data)