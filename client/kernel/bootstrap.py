# -*- coding: utf-8 -*-
import sys
from kernel.initial import entry as kernel_init
from kernel.scheduler import entry as kernel_loop


def main():
    # Initialize stage.
    kernel_init()
    # Execution stage.
    while True:
        try:
            # Loop and run the tasks.
            while True:
                kernel_loop()
        except KeyboardInterrupt:
            print('Exiting...')
            return 0
        except Exception as exc:
            raise exc


if __name__ == '__main__':
    sys.exit(main())
