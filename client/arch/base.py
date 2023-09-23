# -*- coding: utf-8 -*-
from enum import Enum
import platform


class HardwareAbstractLayer:
    class OS(Enum):
        UNKNOWN = 0
        LINUX = 1
        WINDOWS = 2

    def __init__(self):
        self.device_name = 'Unknown'
        self.bits = 8
        self.i2c_buses = {}
        self.pwm_buses = {}
        self.os = self.OS.UNKNOWN
        # Detect the operating system.
        if platform.system() == 'Linux':
            self.os = self.OS.LINUX
        elif platform.system() == 'Windows':
            self.os = self.OS.WINDOWS
