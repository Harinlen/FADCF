# -*- coding: utf-8 -*-
import importlib
from kernel.exception import LogNoArchError


def load(device_id: str):
    # Try to find the device ID.
    try:
        module = importlib.import_module('arch.{}.core'.format(device_id))
    except ModuleNotFoundError:
        raise LogNoArchError(device_id)
    # Initial the hardware.
    return module.HAL()
