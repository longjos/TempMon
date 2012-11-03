# Temperature sensor montior that publishes to Librato Metrics
# See metrics.librato.com

__author__="jlon"
__date__ ="$Nov 3, 2012 1:07:08 PM$"

# Librato Metrics Library
import librato
# Bindings to Temper1 Temperature Sensor Device
import sensors.pcsensor

from time import sleep
import sys
import ConfigParser

# Load configuration
config = ConfigParser.SafeConfigParser()
config.read('config.ini')

def c_to_f(celcius):
    """Convert Celcius to Farenheit"""
    # Sensor occasionally returns a false 0 value.
    # In this context we consider 0 an error and do not convert it
    if(celcius < 1):
        return 0

    f = (((9.0/5.0)*celcius) + 32)
    return f

# Verify there are two sensors available
if(sensors.pcsensor.get_device_count() < 2):
    print "Two sensor devices required\n"
    sys.exit(0)
print "Sensors Detected\n"

print "Connecting to Metrics\n"
# Connect to Librato
connection = librato.LibratoConnection(config.get('metrics', 'user_name'), config.get('metrics', 'api_key'))

# Get a Gauge object for the WaterIn Metric
sensorA = connection.get_gauge("WaterIn")
# Get a Gauge object for the WaterOut Metric
sensorB = connection.get_gauge("WaterOut")

print "Connected\n"

# Loop, reporting the water temps every second
while True:
    tempA = c_to_f(sensors.pcsensor.read_temperature_c(0))
    if(tempA > 1):
        sensorA.add(tempA)

    tempB = c_to_f(sensors.pcsensor.read_temperature_c(1))
    if(tempB > 1):
        sensorB.add(tempB)
        
    sleep(1)
