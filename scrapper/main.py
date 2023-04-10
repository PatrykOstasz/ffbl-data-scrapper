import pandas as pd

from edgedriver import EdgeDriver

def __main__():
    ed = EdgeDriver()
    ed.startScrapping()
    ed.getScrappedData()

    print(ed._scrappedData)