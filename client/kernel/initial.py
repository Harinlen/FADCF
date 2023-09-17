# -*- coding: utf-8 -*-
import psutil
import math
import sys
import importlib
import platform
from mem import MemoryProxy
from lib.logging import info as log_info
from lib.upgrade import upgrade_end
import kernel.version as version


def entry(mem_proxy: MemoryProxy):
    # Finalize upgrade when necessary.
    upgrade_end()
    # Extract the config from memory.
    conf = mem_proxy.get('conf')
    # Loaded hardware architecture functions.
    from arch import load as arch_load
    hal = mem_proxy.set('hal', arch_load(conf.ARCH))
    # Show the system information.
    log_info('FADCF', version.SYSTEM_VERSION, '{}-bit'.format(hal.bits))
    log_info('Core Kernel version: {}.{}.{}'.format(
        version.KERNEL_MAJOR, version.KERNEL_MINOR, version.KERNEL_PATCH))
    log_info('Hardware:', hal.device_name)
    python_bits = int(math.log2(sys.maxsize)) + 1
    log_info('Python Version:', platform.python_version(), '{}-bit'.format(python_bits))
    log_info('Memory:', psutil.virtual_memory().total // 1048576, 'MiB')
    # Load the usr init source code.
    try:
        user_init = importlib.import_module('usr.init')
    except ModuleNotFoundError:
        # No user init module found.
        return
    # Call the main function inside the module.
    if hasattr(user_init, 'main'):
        # Call the main function.
        user_init.main(mem_proxy)
