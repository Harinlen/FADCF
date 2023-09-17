# -*- coding: utf-8 -*-

class RuntimeLogError(Exception):
    def __init__(self, *args): # real signature unknown
        super().__init__(*args)


class CriticalLogError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def dump(self):
        return ''


class LogNoModuleError(CriticalLogError):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def dump(self):
        return 'No module name "{}"'.format(self.name)


class LogNoArchError(CriticalLogError):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def dump(self):
        return 'Architecture "{}" not support.'.format(self.name)


class LogKeyboardInterrupt(Exception):
    pass
