# -*- coding: utf-8 -*-

class RuntimeLogError(Exception):
    def __init__(self, *args): # real signature unknown
        super().__init__(*args)


class CriticalLogError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class LogGeneralError(CriticalLogError):
    def __init__(self, text: str):
        self.error_text = text

    def __str__(self):
        return self.error_text


class LogNoModuleError(CriticalLogError):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __str__(self):
        return 'Failed to find Python module "{}"'.format(self.name)


class LogNoArchError(CriticalLogError):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __str__(self):
        return 'Architecture "{}" not support.'.format(self.name)


class LogNoBusError(CriticalLogError):
    def __init__(self, bus_name: str, bus_id: int):
        super().__init__()
        self.bus_name = bus_name
        self.bus_id = bus_id

    def __str__(self):
        return '{} bus {} does not exist.'.format(self.bus_name, self.bus_id)


class LogSchedulerLoadFailError(LogGeneralError):
    pass


class LogKeyboardInterrupt(Exception):
    pass
