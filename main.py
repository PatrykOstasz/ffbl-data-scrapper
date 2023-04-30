from admin.administrator import Administrator


administrator = Administrator()
administrator.startScraping()
administrator.print()
administrator.saveToFile()