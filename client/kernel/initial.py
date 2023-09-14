# -*- coding: utf-8 -*-
import sys
from kernel.upgrade import upgrade_end


def entry():
    # Finalize upgrade when necessary.
    upgrade_end()
    # Debug.
    sys.exit(0)
    # Initial buses.
    pass
