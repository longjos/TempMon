# Base sensor class providing the basic functions and a bit of an interface
class Sensor(object):
    """Base Sensor Class"""
    def _readTemp (self):
        """Read the value from the device
        Always return in Celcius"""
        raise NotImplementedError("Must be implemented by a sensor driver")
    
    def getTempF (self):
        """ Read the temperature from the sensor and return Farienheit """
        f = (((9.0 / 5.0) * self.getTempC()) + 32)
        return f
    
    def getTempC (self):
        """ Read the temperature from the sensor and return Celcius """
        c = self._readTemp()
        return c
    
    
    