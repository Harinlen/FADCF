# -*- coding: utf-8 -*-
import subprocess


def get_output(*args):
	return subprocess.check_output(args)
