# -*- coding: utf-8 -*-
import os
from lib.commands import get_output
from arch.base import HardwareAbstractLayer
from kernel.exception import LogNoModuleError


class HAL(HardwareAbstractLayer):
    def __init__(self):
        super().__init__()
        if self.os != self.OS.LINUX:
            raise RuntimeError('Raspberry PI HAL only supports Linux.')

        # Initial the device name.
        device_name_bytes, _ = get_output('cat', '/sys/firmware/devicetree/base/model')
        self.device_name = device_name_bytes.decode('ascii')
        os_bits, _ = get_output('getconf', 'LONG_BIT')
        self.bits = int(os_bits.decode('ascii').strip())
        # Get all the /dev files.
        devs = os.listdir('/dev')

        # Loaded buses.
        def load_i2c():
            # Load the SMBus library.
            try:
                from bus.i2c_smbus import BusI2CSmbus
            except ModuleNotFoundError as exc:
                raise LogNoModuleError(exc.name)
            i2c_proxy = {}
            # Find all I2C devices from /dev list
            for i2c_channel in filter(lambda x: x.startswith('i2c-'), devs):
                i2c_id = i2c_channel[4:]
                if i2c_id.isnumeric():
                    # Try to load the channel use SMBus2.
                    i2c_id = int(i2c_id)
                    i2c_proxy[i2c_id] = BusI2CSmbus(bus_id=i2c_id)
            self.i2c_buses = i2c_proxy

        load_i2c()
