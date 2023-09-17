# -*- coding: utf-8 -*-

class HardwareAbstractLayer:
    def __init__(self):
        self.device_name = 'Unknown'
        self.bits = 8
        self.i2c_buses = []
