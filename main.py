from admin.administrator import Administrator

#from admin.webdriverparameters import WebDriverParameters

administrator = Administrator()
administrator.startScraping()
administrator.print()
administrator.saveToFile()

#haha = WebDriverParameters()
