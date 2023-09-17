# -*- coding: utf-8 -*-
import os
import sys
import importlib


def main():
    # Change the working directory.
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    
    from kernel.exception import (RuntimeLogError, CriticalLogError,
                                  LogKeyboardInterrupt)
    from lib.upgrade import UpgradeStart

    def __backbone():
        # Extract the memory access proxy.
        import kernel.mem as mem
        # Initial the system Memory.
        __mem = mem.Memory()
        mem_proxy = __mem.get_proxy()
        # Initial the system Configuration.
        # Read the user configure, and overwrite the system default setting.
        import kernel.conf as default_conf
        conf = default_conf
        try:
            user_conf = importlib.import_module('usr.conf')
            conf.__dict__.update(user_conf.__dict__)
        except ModuleNotFoundError:
            pass
        mem_proxy.set('conf', conf)
        # Initial the system Storage directory structure.
        from kernel.paths import DIR_STORAGE, ensure_dir
        ensure_dir(DIR_STORAGE,
                   'Failed to create storage directory.')
        # Initial the Logging service.
        from lib.logging import (runtime_error_dump, flush as log_flush,
                                 critical_error_dump, logging_start, info)
        logging_start(mem_proxy)
        try:
            # Initial the platform.
            from kernel.initial import entry as platform_init
            platform_init(mem_proxy)
            # Create the scheduler for the task.
            from kernel.scheduler import get_scheduler
            scheduler = get_scheduler(mem_proxy)
            # Loop and run the tasks.
            while True:
                # Run the user tasks.
                scheduler.execute()
                # Flush the logging buffer.
                log_flush()
        except RuntimeLogError as runtime_exc:
            runtime_error_dump(runtime_exc)
            raise
        except CriticalLogError as critical_exc:
            critical_error_dump(critical_exc)
            raise
        except KeyboardInterrupt:
            info('Shutting down')
            raise LogKeyboardInterrupt()

    while True:
        try:
            __backbone()
        except LogKeyboardInterrupt:
            # Keyboard Ctrl+C exit.
            return 0
        except UpgradeStart:
            # Exit the current client to upgrade the system.
            return 0
        except RuntimeLogError:
            # Try to restart the kernel.
            pass
        except CriticalLogError as exc:
            # Critical error happens, need to stop.
            print('Critical error:', exc.dump())
            return 1
        except Exception as exc:
            raise exc


if __name__ == '__main__':
    sys.exit(main())
