# -*- coding: utf-8 -*-
from arch.base import HardwareAbstractLayer
from kernel.exception import LogNoModuleError


class HAL(HardwareAbstractLayer):
    def __init__(self):
        super().__init__()
        # Initial the device name.
        self.device_name = 'Raspberry Pi'
        # Loaded buses.
        self.load_i2c()

    def load_i2c(self):
        try:
            from bus.i2c_smbus import BusI2CSmbus
            self.i2c_buses = [BusI2CSmbus(bus_id=1)]
        except ModuleNotFoundError as exc:
            raise LogNoModuleError(exc.name)
