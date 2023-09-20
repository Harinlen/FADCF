# -*- coding: utf-8 -*-
import os
import sys
import shutil
import subprocess


def main():
    # Check runtime directory.
    dir_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_runtime = os.path.join(dir_root, 'runtime')
    if os.path.isdir(dir_runtime):
        if input('Runtime directory is already created, reinstall? [Y/n]: ').lower() != 'y':
            return 0
        # remove the runtime directory.
        shutil.rmtree(dir_runtime)
    # Create the venv for the client.
    print('Creating venv...')
    os.chdir(dir_root)
    subprocess.run([sys.executable, '-m', 'venv', 'runtime'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
