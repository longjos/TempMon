# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
from sensors.DummySensor import DummySensor


class  TestSensorTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = TestSensor()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_testSensorC(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        sensor = DummySensor()
        self.assertEqual(1, sensor.getTempC())

    def test_testSensorF(self):
        sensor = DummySensor()
        self.assertEqual(33.8, sensor.getTempF())
        
if __name__ == '__main__':
    unittest.main()

