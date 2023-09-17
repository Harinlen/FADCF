# -*- coding: utf-8 -*-
import psutil
import platform
from lib.logging import info as log_info
from lib.upgrade import upgrade_end
import kernel.version as version
import kernel.conf as conf


def entry():
    # Finalize upgrade when necessary.
    upgrade_end()
    # Extract the memory access proxy.
    from kernel.mem import usr
    mem = usr.get_proxy()
    # Loaded hardware architecture functions.
    from arch import load as arch_load
    hal = mem.set('hal', arch_load(conf.ARCH))
    # Show the system information.
    log_info('FADCF', version.SYSTEM_VERSION, '{}-bit'.format(hal.bits))
    log_info('Core Kernel version: {}.{}.{}'.format(
        version.KERNEL_MAJOR, version.KERNEL_MINOR, version.KERNEL_PATCH))
    log_info('Hardware:', hal.device_name)
    log_info('Python Version:', platform.python_version())
    log_info('Memory:', psutil.virtual_memory().total // 1048576, 'MiB')
