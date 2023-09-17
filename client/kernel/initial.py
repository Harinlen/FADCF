# -*- coding: utf-8 -*-
from lib.logging import info as log_info
from lib.upgrade import upgrade_end
import kernel.version as version


def entry():
    # Finalize upgrade when necessary.
    upgrade_end()
    # Show the version information.
    log_info('FADCF', version.SYSTEM_VERSION)
    log_info('Core Kernel version: {}.{}.{}'.format(
        version.KERNEL_MAJOR, version.KERNEL_MINOR, version.KERNEL_PATCH))
    # Extract the memory access proxy.
    from kernel.mem import usr
    mem = usr.get_proxy()
    # Loaded hardware architecture functions.
    from arch import load as arch_load
    hal = mem.set('hal', arch_load('x86'))
    # Print the hardware info.
    log_info('Hardware:', hal.device_name)
