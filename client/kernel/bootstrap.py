# -*- coding: utf-8 -*-
import sys

from kernel.exception import (RuntimeLogError, CriticalLogError,
                              LogKeyboardInterrupt)
from kernel.initial import entry as kernel_init
from kernel.scheduler import get_scheduler
from kernel.paths import DIR_STORAGE, ensure_dir
from lib.logging import (runtime_error_dump, flush as log_flush,
                         critical_error_dump, logging_start, info)
from lib.upgrade import UpgradeStart
import kernel.mem as mem


def main():
    def __backbone():
        # Check the path availability.
        ensure_dir(DIR_STORAGE, 'Failed to create storage directory.')
        # Start logging service.
        logging_start()
        try:
            # Create the shared memory.
            mem.usr = mem.Memory()
            # Start the kernel source codes.
            try:
                # Initialize stage.
                kernel_init()
                # Create the scheduler for the task.
                scheduler = get_scheduler()
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
