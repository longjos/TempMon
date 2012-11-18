# Temperature sensor montior that publishes to Librato Metrics
# See metrics.librato.com

__author__="jlon"
__date__ ="$Nov 3, 2012 1:07:08 PM$"

# Librato Metrics Library
import librato
# Import the Temper device class
from sensors.Temper import *

from time import sleep
import sys
import ConfigParser

# Load configuration
config = ConfigParser.SafeConfigParser()
config.read('config.ini')

# Verify there are two sensors available
# If not, try again after 10 seconds
# This allows for the sensors to be plugged in after removing a keyboard
while (Temper.availableDeviceCount < 1):
    print "Two sensor devices required\n"
    sleep(10)
print "Sensors Detected\n"

print "Connecting to Metrics\n"
# Connect to Librato
# connection = librato.LibratoConnection(config.get('metrics', 'user_name'), config.get('metrics', 'api_key'))

# Get a Gauge object for the WaterIn Metric
# sensorA = connection.get_gauge("WaterIn")
# Get a Gauge object for the WaterOut Metric
# sensorB = connection.get_gauge("WaterOut")

print "Connected\n"

# Connect to the sensors
try: 
    deviceA = Temper()
except NoDevicesAvailableException:
    print "Unable to connect to device"
    exit()


# Loop, reporting the water temps every second
while True:
    try:
        tempA = deviceA.getTempF()
    except:
        print "Error reading from device A"
    print "A: {}".format(tempA)
#        try:
#            tempB = c_to_f(sensors.pcsensor.read_temperature_c(1))
#        except:
#            print "Error reading from device B"

#        if(tempA > 1):
#            sensorA.add(tempA)
#        if(tempB > 1):
#            sensorB.add(tempB)        
    sleep(10)
