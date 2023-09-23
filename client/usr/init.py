# -*- coding: utf-8 -*-
import sys
from kernel.mem import MemoryProxy


def main(mem: MemoryProxy):
    # Load the sensor.
    hal = mem.hal()

    sys.exit(0)
