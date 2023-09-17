# -*- coding: utf-8 -*-

class RuntimeLogError(Exception):
    def __init__(self, *args): # real signature unknown
        super().__init__(*args)


class CriticalLogError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def dump(self):
        return ''


class LogGeneralError(CriticalLogError):
    def __init__(self, text: str):
        self.error_text = text

    def dump(self):
        return self.error_text


class LogNoModuleError(CriticalLogError):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def dump(self):
        return 'Failed to find Python module "{}"'.format(self.name)


class LogNoArchError(CriticalLogError):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def dump(self):
        return 'Architecture "{}" not support.'.format(self.name)


class LogSchedulerLoadFailError(LogGeneralError):
    pass


class LogKeyboardInterrupt(Exception):
    pass
