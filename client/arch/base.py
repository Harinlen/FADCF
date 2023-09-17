# -*- coding: utf-8 -*-

class HardwareAbstractLayer:
    def __init__(self):
        self.device_name = 'Unknown'
        self.i2c_buses = []

    def load_i2c(self):
        pass
