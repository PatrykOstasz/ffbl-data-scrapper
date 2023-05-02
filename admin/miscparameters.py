from admin.parameterparser import ParameterParser


def validate(misc):
    keys = ['driver.waittime.min',
            'driver.waittime.max']
    try:
        for k in keys:
            value = misc[k]
    except KeyError as err:
        print('Exception Caught! Value for specific key is not found!')
        raise
   

class MiscParameters:
    def __init__(self) -> None:
        self._misc = ParameterParser().getMiscParams()

    @property
    def waitTimeMin(self):
        return self._misc['driver.waittime.min']

    @property
    def waitTimeMax(self):
        return self._misc['driver.waittime.max']
    