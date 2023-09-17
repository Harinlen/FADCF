# -*- coding: utf-8 -*-
import os

DIR_KERNEL = os.path.dirname(os.path.abspath(__file__))
DIR_ROOT = os.path.dirname(DIR_KERNEL)
DIR_STORAGE = os.path.join(DIR_ROOT, 'storage')


class DirCreateFailed(Exception):
    def __init__(self, message):
        super().__init__(message)


def ensure_dir(dir_path: str, failed_message: str = ''):
    try:
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path, exist_ok=True)
    except OSError:
        raise DirCreateFailed(failed_message)
