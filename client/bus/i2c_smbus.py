# -*- coding: utf-8 -*-
from bus.i2c import BusI2C
import smbus2


class BusI2CSmbus(BusI2C):
    def __init__(self, bus_id: int):
        super().__init__(bus_id)
        self.__smbus = smbus2.SMBus(bus=bus_id)
