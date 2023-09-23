# -*- coding: utf-8 -*-

class BusI2C:
    def __init__(self, bus_id: int):
        self.bus_id = bus_id

    def write(self, i2c_addr, register, value):
        pass
