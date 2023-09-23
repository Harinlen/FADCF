# -*- coding: utf-8 -*-
import subprocess


def get_output(*args):
    result = None
    output_exc = None
    try:
        result = subprocess.check_output(args)
    except Exception as exc:
        output_exc = exc
    return result, output_exc
