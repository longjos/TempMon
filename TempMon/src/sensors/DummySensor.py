
# A dummy test sensor that will always return 1 degree Celcius

from sensors.Sensor import Sensor

class DummySensor(Sensor):
    """ Dummy test sensor, always return 1 degree celcius """
    
    def _readTemp(self):
        return 1