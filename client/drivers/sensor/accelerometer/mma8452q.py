# -*- coding: utf-8 -*-
from base import SensorAccelerometer
from arch.base import HardwareAbstractLayer
from kernel.exception import LogNoBusError


class Driver(SensorAccelerometer):
    def __init__(self, hal: HardwareAbstractLayer, i2c_bus_id: int):
        # Load the I2C channel.
        if i2c_bus_id not in hal.i2c_buses:
            raise LogNoBusError('I2C', i2c_bus_id)
        # Load the bus from the HAL.
        self.__bus = hal.i2c_buses[i2c_bus_id]

    def begin(self):
        # Configure the bus.
        # MMA8452Q address, 0x1C(28)
        # Select Control register, 0x2A(42)
        #		0x00(00)	StandBy mode
        self.__bus.write(0x1C, 0x2A, 0x00)
        # MMA8452Q address, 0x1C(28)
        # Select Control register, 0x2A(42)
        #		0x01(01)	Active mode
        self.__bus.write(0x1C, 0x2A, 0x01)
        # MMA8452Q address, 0x1C(28)
        # Select Configuration register, 0x0E(14)
        #		0x00(00)	Set range to +/- 2g
        self.__bus.write(0x1C, 0x0E, 0x00)
