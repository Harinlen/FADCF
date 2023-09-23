# -*- coding: utf-8 -*-
import sys
from kernel.mem import MemoryProxy


def main(mem: MemoryProxy):
    # Load the sensor.
    hal = mem.hal()
    print(hal.i2c_buses)
    from drivers.sensor.accelerometer.mma8452q import Driver
    driver = Driver(hal, 1)
    driver.begin()
    sys.exit(0)
