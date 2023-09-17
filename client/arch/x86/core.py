# -*- coding: utf-8 -*-
from arch.base import HardwareAbstractLayer


class HAL(HardwareAbstractLayer):
    def __init__(self):
        super().__init__()
        # Initial the device name.
        self.device_name = 'Generic x86 Device'
        self.bits = 64
