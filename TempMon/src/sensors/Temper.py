
# Driver for the Temper 1 temperature sensor

from sensors.Sensor import Sensor
from sensors import pcsensor

class Temper(Sensor):
    """ Using the pcsensor bindings read temperature from a Temper1 device """
    
    deviceID = None
    
    @staticmethod
    def availableDeviceCount():
        return pcsensor.get_device_count()
    
    def __init__(self, deviceID = None):
        
            
        if Temper.availableDeviceCount() > 0:
            if deviceID is None:
                if Temper.deviceID is None:
                    Temper.deviceID = 0
                    self.deviceID = 0
                else:
                    if Temper.availableDeviceCount() < (Temper.deviceID + 1):
                        raise NoDevicesAvailableException("No more devices available")
                    else:
                        self.deviceID = Temper.deviceID + 1
            else:
                self.deviceID = deviceID
        else:
            raise NoDevicesAvailableException("No Temper1 Devices Available")
                    
        
    def _readTemp(self):
        """ Read the temp using the pcsensor bindings
        Return the value in Celcius """
        readData = True
        while readData:
            readTemp = pcsensor.read_temperature_c(self.deviceID)
            if readTemp > 0:
                readData = False
                return readTemp
    
    def getDeviceID(self):
        """ Return the device ID for this instance """
        return self.deviceID
    
class NoDevicesAvailableException(Exception):
    """ No Devices available """