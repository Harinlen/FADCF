# -*- coding: utf-8 -*-
import os
from lib.commands import get_output
from arch.base import HardwareAbstractLayer
from kernel.exception import LogNoModuleError


class HAL(HardwareAbstractLayer):
    def __init__(self):
        super().__init__()
        # Initial the device name.
        self.device_name = get_output('cat', '/sys/firmware/devicetree/base/model').decode('ascii')
        self.bits = int(get_output('getconf', 'LONG_BIT').decode('ascii').strip())
        # Get all the /dev files.
        devs = os.listdir('/dev')
        # Loaded buses.
        self.load_i2c(devs)

    def load_i2c(self, devs: list):
        # Load the SMBus library.
        try:
            from bus.i2c_smbus import BusI2CSmbus
        except ModuleNotFoundError as exc:
            raise LogNoModuleError(exc.name)
        i2c_proxy = []
        # Find all I2C devices from /dev list
        for i2c_channel in filter(lambda x: x.startswith('i2c-'), devs):
            i2c_id = i2c_channel[4:]
            if i2c_id.isnumeric():
                # Try to load the channel use SMBus2.
                i2c_proxy.append(BusI2CSmbus(bus_id=int(i2c_id)))
        self.i2c_buses = i2c_proxy
