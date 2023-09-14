# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import pickle
import hashlib
from kernel.paths import DIR_STORAGE, DIR_KERNEL
from kernel.mem import usr

USR_SWAP_PATH = os.path.join(DIR_STORAGE, 'usr_swap')
USR_SWAP_HASH_PATH = os.path.join(DIR_STORAGE, 'usr_swap.md5')


class UpgradeStart(Exception):
    pass


def upgrade_start():
    # Save the user object to swap.
    with open(USR_SWAP_PATH, 'wb') as usr_swap_file:
        pickle.dump(usr, usr_swap_file)
    # Save the checksum of the HASH.
    with open(USR_SWAP_HASH_PATH, 'w') as usr_swap_hash_file:
        usr_swap_hash_file.write(hashlib.md5(open(USR_SWAP_PATH, 'rb').read()).hexdigest())
    # Create the upgrade flag.

    # Start the upgrade process.
    subprocess.Popen([sys.executable, __file__], cwd=os.getcwd())
    # Mark the system upgrade status.
    raise UpgradeStart


def upgrade_end():
    pass


def upgrade_main():
    # Update the client source code.
    pass
    # Restart the system.
    subprocess.Popen([sys.executable, os.path.join(DIR_KERNEL, 'bootstrap.py')], cwd=os.getcwd())
    return 0


if __name__ == '__main__':
    sys.exit(upgrade_main())
